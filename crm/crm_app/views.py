from django.shortcuts import render
from django.views import View
from .forms import ContactForm

# Create your views here.
class contact_view(View):
	def get(self, request, *args, **kwargs):
		self.template_name = 'crm_app/contact.html'
		form = ContactForm()
		context = {"form":form}
		return render(request, self.template_name, context)
