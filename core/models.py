import uuid

from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models


# Create your models here.


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, default=None)
    legal_number = models.CharField(max_length=100, default=None)
    logo = models.ImageField(upload_to='logo/', default=None)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('core:company')


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, default=None)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('core:department')


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')

    )
    gender = models.CharField(max_length=1, choices=GENDER)
    # department = models.ForeignKey(Department, on_delete=models.PROTECT)
    # company = models.ForeignKey(Company, on_delete=models.PROTECT)
    phone = models.CharField(max_length=14, default='Sem Telefone')
    role = models.CharField(max_length=50, default='Sem Atribuição')
    age = models.IntegerField(default=0)
    joining_date = models.DateField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    # Simple title return queue for django admin or auto template
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('core:employee')
