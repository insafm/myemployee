from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.views.generic.edit import DeleteView

from .forms import AddEmployeeForm, AddEmployeeSalaryForm
from .models import Employee
from .tables import EmployeeTable

@method_decorator(login_required, name='dispatch')
class CreateUpdateEmployee(View):
	template = 'dashboard_form_wrapper.html'
	context = {}
	context['label'] = _('Add New Employee')
	def get(self, request, *args, **kwargs):
		instance = None
		if kwargs.get("uuid"):
			instance = Employee.objects.filter(uuid=kwargs.get("uuid")).first()
		
		form = AddEmployeeForm(request.POST or None, instance=instance)

		self.context['title']       = _("New Employee")
		self.context['form'] = form

		return render(request, self.template, self.context)

	def post(self, request, *args, **kwargs):
		instance = None
		if kwargs.get("uuid"):
			instance = Employee.objects.filter(uuid=kwargs.get("uuid")).first()
		
		form = AddEmployeeForm(request.POST or None, instance=instance)

		if form.is_valid():
			employee = form.save()

			# Save created employee id into user session
			if employee:
				# messages.add_message(request, messages.INFO, _("Please update employee salary details.."))
				request.session['latest_employee_id'] = employee.id
				return redirect(reverse("employee:add_employee_salary"))

		return render(request, self.template, context={'form': form})

@method_decorator(login_required, name='dispatch')
class CreateUpdateEmployeeSalary(View):
	template = 'dashboard_form_wrapper.html'
	context = {}
	context['label'] = _('Add Employee salary')

	def get(self, request, *args, **kwargs):

		latest_employee_id = request.session.get("latest_employee_id")
		if latest_employee_id:
			# Employee id found in user session.
			employee = Employee.objects.filter(id=latest_employee_id).first()
			if employee:
				initial = {
					'employee': employee,
				}
				salary_form = AddEmployeeSalaryForm(request.POST or None, initial=initial)
				self.context['title'] = _(f"Employee Salary - {employee.name}")
				self.context['form'] = salary_form

				return render(request, self.template, self.context)

		# Employee id not found in user session.
		return redirect("employee:add_employee")

	def post(self, request, *args, **kwargs):
		latest_employee_id = request.session.get("latest_employee_id")
		if latest_employee_id:
			# Employee id found in user session.
			employee = Employee.objects.filter(id=latest_employee_id).first()
			if employee:
				initial = {
					'employee': employee,
					'amount': employee,
				}
				
		form = AddEmployeeSalaryForm(request.POST or None, initial=initial)
		if form.is_valid():
			form.save()

			# Reset last employee id from session
			if "latest_employee_id" in request.session:
				request.session.pop("latest_employee_id")
				
			messages.add_message(request, messages.SUCCESS, _("Employee details added successfully."))
			return redirect("employee:list_employee")
		return render(request, self.template, context={'form': form})
	

@method_decorator(login_required, name='dispatch')
class EmployeesList(View):
	"""List the employees, with 10 employees per page."""
	
	model = Employee
	table_class = EmployeeTable
	template_name = 'table.html'

	def get(self, request, *args, **kwargs):
		queryset = self.model.objects.filter(status=True, deleted=False)
		table = self.table_class(queryset)
		table.paginate(page=request.GET.get("page", 1), per_page=settings.DATATABLE.get('per_page', 10))
		return render(request, self.template_name, {"table": table, "title": "Employees"})

@method_decorator(login_required, name='dispatch')
class ViewEmployee(View):
	"""View details of an employee"""
	template_name = 'employee/view_employee.html'
	context = {}

	def get(self, request, *args, **kwargs):
		self.context['title']       = _("Employee Details")
		instance = None
		if kwargs.get("uuid"):
			instance = Employee.objects.filter(uuid=kwargs.get("uuid")).first()
			if instance:
				self.context['instance'] = instance
				return render(request, self.template_name, self.context)
		messages.add_message(request, messages.ERROR, _("Some error occured."))
		return redirect("employee:list_employee")
		

@method_decorator(login_required, name='dispatch')
class DeleteEmployee(DeleteView):
	"""Delete an employee"""
	model = Employee
	slug_url_kwarg = 'uuid'
	slug_field = 'uuid'
	success_url = reverse_lazy("employee:list_employee")
	success_message = _("Employee was deleted successfully.")

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super().delete(request, *args, **kwargs)