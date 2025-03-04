from django.contrib import admin
from guest.models import Employee, Branch,Guest

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'branch', 'email_id')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Branch)
admin.site.register(Guest)