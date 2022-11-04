from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from .models import Employee, Salary

class AddEmployeeForm(forms.ModelForm):
	"""Employee form
	"""
	class Meta:
		model = Employee
		fields = ['first_name', 'last_name', 'code', 'gender', 'department', 'phone_number', 'address', ]


class AddEmployeeSalaryForm(forms.Form):
	"""Employee salary form
	"""
	first_name = forms.CharField(disabled=True, required=False)
	last_name = forms.CharField(disabled=True, required=False)
	code = forms.CharField(disabled=True, required=False)
	salary = forms.DecimalField()

	def __init__(self, *args, **kwargs):
		self.employee = kwargs.get('initial').get("employee") if kwargs else None
		super().__init__(*args, **kwargs)
		
		if self.employee:
			self.fields['first_name'].initial = self.employee.first_name
			self.fields['last_name'].initial = self.employee.last_name
			self.fields['code'].initial = self.employee.code
			if hasattr(self.employee, "employee_salary") and self.employee.employee_salary.amount:
				self.fields['salary'].initial = self.employee.employee_salary.amount
	
	def clean_salary(self):
		salary = self.cleaned_data.get("salary")
		if salary >= 1000000000:
			raise ValidationError(_('Enter salary amount below 1000000000.'))
		return salary

	def save(self):
		instance = None
		print("self.cleaned_data:: ", self.cleaned_data)
		if self.employee and self.cleaned_data.get("salary"):
			instance = Salary.objects.update_or_create(employee=self.employee, defaults={'amount': self.cleaned_data['salary']})
		return instance