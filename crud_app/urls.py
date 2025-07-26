from django.urls import path
from .views import *

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('create_employee/', create_employee, name='create_employee'),
    path('update_employee/<int:emp_id>/', update_employee, name='update_employee'),
    path('delete_employee/<int:emp_id>/', delete_employee, name='delete_employee'),
    
]