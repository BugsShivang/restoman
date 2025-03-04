from django.urls import path
from .views import *

urlpatterns = [
    # Guest URLs
    path('add-guest/', add_guest, name='add-guest'),
    path('update-guest/<int:pk>/', update_guest, name='update-guest'),
    path('signed-in-guests/', signed_in_guests, name='signed-in-guests'),
    path('signed-out-guests/', signed_out_guests, name='signed-out-guests'),
    path('guest-sign-out/<int:pk>/', guest_sign_out, name='guest-sign-out'),
    path('export-csv', export_csv, name='export-csv'),
    path('search-guests/', search_guests, name='search-guests'),

    # Branch URLs
    path('add-branch/', add_branch, name='add-branch'),

    # Employee URLs
    path('add-employee/', add_employee, name='add-employee'),
    path('update-employee/<int:pk>/', update_employee, name='update-employee'),
    path('signed-in-employees/', signed_in_employees, name='signed-in-employees'),
    # path('signed-out-employees/', signed_out_employees, name='signed-out-employees'),
    path('sign-out-employee/<int:pk>/', sign_out_employee, name='sign-out-employee'),
]
