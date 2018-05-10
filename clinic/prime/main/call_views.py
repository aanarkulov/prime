from urllib.parse import quote_plus
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from .models import *

class TreatmentDetailView(DetailView):
	template_name = 'treatment-inner.html'
	def get_object(self, *args, **kwargs):
		slug = self.kwargs.get("slug")
		instance = get_object_or_404(Treatment, slug=slug)
		return instance