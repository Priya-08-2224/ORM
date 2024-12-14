from django.db import models
from django.contrib import admin
class Bank_loan(models.Model):
    Accno=models.IntegerField()
    name=models.CharField(max_length=100)
    mobileno=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    

class Bank_loanAdmin(admin.ModelAdmin):
    list_display=('Accno','name','mobileno','age','email')
    