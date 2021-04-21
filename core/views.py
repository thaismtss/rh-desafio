from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from core.models import Company, Employee, Department


def index(request):
    return render(request, 'core/index.html')


def select_company(request):
    company = Company.objects.all()
    return render(request, 'core/employee.html', {'company': company})


class UserCreate(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'core/user_form.html'
    success_url = '/login'


class CompanyCreate(CreateView):
    model = Company
    fields = ['name', 'legal_number', 'logo']


class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name', 'legal_number', 'logo']
    success_url = '/company'


class CompanyDetail(DetailView):
    model = Company


class CompanyDelete(DeleteView):
    model = Company
    success_url = '/company'


class CompanyList(ListView):
    model = Company


class DepartmentCreate(CreateView):
    model = Department
    fields = ['name', 'company', 'admin']


class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['name', 'company', 'admin']
    success_url = '/company/department'


class DepartmentDetail(DetailView):
    model = Department


class DepartmentDelete(DeleteView):
    model = Department
    success_url = '/company/department'


class DepartmentList(ListView):
    model = Department


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'user', 'gender', 'phone', 'age', 'joining_date', 'salary','role', 'department']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.filter(pk=self.kwargs.get("pk")).values_list('name')
        context['logo'] = Company.objects.filter(pk=self.kwargs.get("pk")).values_list('logo')
        return context


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'user', 'gender', 'phone', 'age', 'joining_date', 'salary', 'role', 'department']


class EmployeeDetail(DetailView):
    model = Employee


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = '/company/employee'


class EmployeeList(ListView):
    model = Employee
