from django import forms
from .models import * 

class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'surname', 'email_id', 'phone_number', 'address']

class UpdateGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'surname', 'email_id', 'phone_number', 'address']
        
        
class AddBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name']  # Field for adding a branch name

class UpdateBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name']  # Field for updating branch name
        
class AddEmployeeForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=False)  # Optional field to select an existing branch

    class Meta:
        model = Employee
        fields = ['first_name', 'surname', 'email_id', 'phone_number', 'address', 'salary', 'branch']

class UpdateEmployeeForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=False)  # Optional field to select an existing branch

    class Meta:
        model = Employee
        fields = ['first_name', 'surname', 'email_id', 'phone_number', 'address', 'salary','branch']
