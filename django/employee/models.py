import uuid
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _

class AbstractBaseModel(models.Model):
	"""AbstractBaseModel contains common fields between models.
	All models should extend this class.
	"""
	status = models.BooleanField(default=True, blank=True)
	deleted = models.BooleanField(default=False, blank=True)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)

	class Meta:
		abstract = True


class Department(AbstractBaseModel):
	"""Department represents the sector a set of employees belongs to.
	
	Args:
		AbstractBaseModel (class): contains common fields
	"""

	name = models.CharField(max_length=250, unique=True)

	def __str__(self):
		return self.name


class Employee(AbstractBaseModel):
	"""Employee represents the people from a given department.

	Args:
		AbstractBaseModel (class): contains common fields
	"""

	GENDER_OPTIONS = [
		('M', _("Male")),
		('F', _("Female")),
		('O', _("Other")),
	]
	uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True, null=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	code = models.CharField(max_length=50, unique=True)
	gender = models.CharField(max_length=1, blank=True, choices=GENDER_OPTIONS)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	phone_number = PhoneNumberField(blank=True)
	address = models.TextField(max_length=500, blank=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
	
	@property
	def name(self):
		return f"{self.first_name} {self.last_name}"

class Salary(AbstractBaseModel):
	"""Salary details of each employees

	Args:
		AbstractBaseModel (class): contains common fields
	"""
	employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="employee_salary")
	amount = models.DecimalField(max_digits = 10, decimal_places = 2)