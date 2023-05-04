from django.shortcuts import render
from django.views import View

# Create your views here.
class home(View):
	def get(self, request, *args, **kwargs):
		self.template_name = 'crm_app/home.html'
		return render(request, self.template_name, {})
