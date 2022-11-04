from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
class Home(View):
	"""Homepage view"""
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		return redirect("users:dashboard")

@method_decorator(login_required, name='dispatch')
class Dashboard(View):
	"""Dashboard view after user login, this contains navigation menus."""
	template_name = 'dashboard.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})