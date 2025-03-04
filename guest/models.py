from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Guest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    to_see = models.CharField(max_length=100)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    has_signed_out = models.BooleanField(default=False)
    
    

# Branch Model
class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Fields for tracking employee sign in and out
    is_active = models.BooleanField(default=True)  # Track whether employee is signed in
    time_in = models.DateTimeField(null=True, blank=True)  # When employee signed in
    time_out = models.DateTimeField(null=True, blank=True)  # When employee signed out

    def __str__(self):
        return f"{self.first_name} {self.surname}"


    