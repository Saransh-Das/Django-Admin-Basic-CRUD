from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    eclass = models.CharField(max_length=100 , null=True , blank=False)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=30)
