from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView
from core.views import CompanyList, CompanyCreate, index, \
   DepartmentList, DepartmentCreate, EmployeeList, EmployeeCreate, \
   select_company, DepartmentUpdate, CompanyUpdate, UserCreate

app_name = 'core'

urlpatterns = [
   path('', index, name='home'),
   path('login', LoginView.as_view(template_name='login.html'), name='login'),
   path('register', UserCreate.as_view(), name='register'),
   path('company/', login_required(CompanyList.as_view()), name='company'),
   path('company/create', login_required(CompanyCreate.as_view()), name='company_create'),
   path('company/update/<pk>', login_required(CompanyUpdate.as_view()), name='company_update'),
   path('company/department', login_required(DepartmentList.as_view()), name='department'),
   path('company/department_create', login_required(DepartmentCreate.as_view()), name='department_create'),
   path('company/department_update/<pk>', login_required(DepartmentUpdate.as_view()), name='department_update'),
   path('company/employee', login_required(EmployeeList.as_view()), name='employee'),
   path('company/employee_select_company', select_company, name='select_company'),
   path('company/employee_create/<pk>', login_required(EmployeeCreate.as_view()), name='employee_create'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)