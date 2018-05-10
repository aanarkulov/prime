from django.contrib import auth
from django.conf import settings
from django.contrib import messages
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Client
# from .templatetags.filter import *
from .forms import SignUpForm, LoginForm
import json, jwt, django, base64, random, uuid
from .utils import number_prettify, MyEncoder, send_sms

# Create your views here.
def code_activation(request):
    if 'account_confirm' not in request.session.keys():
        return redirect('register')

    if request.method == 'POST':
        code = request.POST.get('code_activation')
        token = request.COOKIES['CFIRM']
        try:
            verify_token = jwt.decode(token, str(code))
            confirm_client = Client.objects.filter(phone=str(verify_token['client_confirm_telephone'])).first()
            if confirm_client:
                confirm_client.confirmed = True
                confirm_client.save()
                request.session['is_logged_in'] = str(confirm_client.public_id)
                request.session['client_phone'] = str(confirm_client.phone)
                del request.session['account_confirm']
                return redirect('profile')
            else:
                return redirect('code_activation')
        except:
            messages.error(request,_('Wrong code or token is expired'))
            return redirect('code_activation')
    #     data = json.dumps(eval(request.body), cls=MyEncoder)
    #     data_jsonified = json.loads(data)
        
    #     template_snippet = Template('<input type="hidden" name="csrfmiddlewaretoken" value={{csrf_token}}>')
        
    #     csrf_token_html = template_snippet.render(Context({'csrf_token': django.middleware.csrf.get_token(request)}))

    #     html_template = render_to_string('code_activation.html', {'csrf_token': csrf_token_html, 'title':'Confirm account'})

    #     response = HttpResponse(html_template)

    #     active_code = '12345'
    #     token = jwt.encode({'confirmation_account_code' : str('996702822295')}, str(active_code))

    #     response.set_cookie('CFIRM', token)
    #     return response
    else:
        context = {
            'title':'Confirm account'
        }
        return render(request, 'code_activation.html', context)

def login(request):
    if 'is_logged_in' in request.session.keys():
        return redirect('profile')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = number_prettify(request.POST.get('phone'))
            client = Client.objects.filter(phone=telephone).first()
            if client:
                get_password = request.POST.get('password')
                if client.check_password(get_password):
                    request.session['is_logged_in'] = str(client.public_id)
                    next_ =  request.GET.get('next', None)
                    if next_:
                        return redirect(next_)
                    return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'title':'Login'})

def register(request):
    if 'is_logged_in' in request.session.keys():
        return redirect('profile')
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = Client()
            telephone = number_prettify(form.cleaned_data.get('phone'))
            user.phone = telephone
            raw_password = form.cleaned_data.get('password1')
            user.set_password(str(raw_password))
            user.save()

            html_template = render_to_string('code_activation.html', {'csrf_token': django.middleware.csrf.get_token(request), 'title':'Confirm account'})
            response = HttpResponse(html_template)

            # active_code = random.randint(10**(6-1), 10**6-1)
            active_code = '12345'
            token = jwt.encode({'client_confirm_telephone' : str(user.phone), 'exp' : datetime.utcnow() + timedelta(minutes=30)}, str(active_code), algorithm='HS256')
            
            request.session['account_confirm'] = True
            response.set_cookie('CFIRM', token.decode('ascii'))

            # send_sms("""
            #     <?xml version="1.0" encoding="UTF-8"?>
            #     <message>
            #         <login>{}</login>
            #         <pwd>{}</pwd>
            #         <id>{}</id>
            #         <sender>{}</sender>
            #         <text>{}</text>
            #         <phones>
            #             <phone>{}</phone>
            #         </phones>
            #         <test>0</test>
            #     </message>""".format(
            #         settings.SMS_LOGIN,
            #         settings.SMS_PASSWORD,
            #         uuid.uuid4(),
            #         settings.SMS_SENDER,
            #         str(settings.SMS_TEXT.encode('utf-8'))+': ' + str(active_code),
            #         user.phone)
            # )
            
            return response
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'title':'Registration'})

def log_me_out(request):
    if 'is_logged_in' in request.session.keys():
        try:
            del request.session['is_logged_in']
        except KeyError:
            pass
        return redirect("index")
    else:
        return redirect('index')