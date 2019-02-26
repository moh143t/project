from django.db import models

class signUp(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(max_length=25)
    password=models.TextField(max_length=10)

    def __str__(self):
        tem='{0.name}{0.email}{0.password}'
        return (tem.format(self))

