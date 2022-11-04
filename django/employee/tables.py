import django_tables2 as tables
import itertools
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from .models import Employee

class EmployeeTable(tables.Table):
	"""Data table for emloyee lising by using django_tables2 package.
	"""
	counter = tables.Column(verbose_name="#", empty_values=(), orderable=False)
	view_link = tables.TemplateColumn(verbose_name="View", template_name="table_view_button.html")
	edit_link = tables.TemplateColumn(verbose_name="Edit", template_name="table_edit_button.html")
	delete_link = tables.TemplateColumn(verbose_name="Delete", template_name="table_delete_button.html")

	def render_counter(self):
		self.row_counter = getattr(self, 'row_counter', itertools.count(start=self.page.start_index()))
		return next(self.row_counter)
	
	def render_edit_link(self, record, value, column, bound_column, bound_row):
		value = {
			'label': "Edit",
			'url_reverse': "employee:edit_employee",
			'key': record.uuid,
		}
		return mark_safe(
			column.render(record, self, value, bound_column, bound_row=bound_row)
		)

	def render_view_link(self, record, value, column, bound_column, bound_row):
		value = {
			'label': "View",
			'url_reverse': "employee:view_employee",
			'key': record.uuid,
		}
		return mark_safe(
			column.render(record, self, value, bound_column, bound_row=bound_row)
		)

	def render_delete_link(self, record, value, column, bound_column, bound_row):
		value = {
			'label': "Delete",
			'url_reverse': "employee:delete_employee",
			'key': record.uuid,
		}
		return mark_safe(
			column.render(record, self, value, bound_column, bound_row=bound_row)
		)

	class Meta:
		model = Employee
		template_name = "django_tables2/bootstrap-responsive.html"
		fields = ['first_name', 'last_name', 'code', 'gender', 'department', 'phone_number', ]
		sequence = ('counter', '...')
		empty_text = _("There are no data to display.")