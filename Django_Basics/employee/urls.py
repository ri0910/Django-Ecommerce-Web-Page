from django.urls import path
from employee import views

urlpatterns = [
    path('<int:pk>', views.employee_detail, name='employee_detail')
]
