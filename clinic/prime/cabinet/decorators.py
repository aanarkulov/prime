from django.shortcuts import redirect
from functools import wraps

def login_required():
	def wrapper(fn):
		@wraps(fn)
		def decorated_view(request, *args, **kwargs):
			if 'is_logged_in' not in request.session.keys():
				return redirect('login')
			return fn(request, *args, **kwargs)
		return decorated_view
	return wrapper