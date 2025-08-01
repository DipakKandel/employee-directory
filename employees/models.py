from django.db import models

# Create your tables  here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20,blank=True)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100, choices=[('Manager', 'Manager'), ('Developer', 'Developer'), ('Designer', 'Designer'), ('HR', 'HR'), ('Other', 'Other')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name+" "+self.last_name

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name