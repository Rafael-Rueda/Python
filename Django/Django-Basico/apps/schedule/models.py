from django.db import models
from django.contrib.auth.models import User

class schedule_category(models.Model):
    category_choices = [
        ('Personal', 'Personal'),
        ('Professional', 'Professional'),
        ('Entertainment', 'Entertainment'),
        ('Family', 'Family'),
        ('Friends', 'Friends'),
    ]
    category = models.CharField(choices=category_choices, default='personal', max_length=50)

    def __str__(self):
        return self.category

class scheduleManager(models.Manager):
    def get_user_schedules(self, user):
        return self.filter(author = user).order_by('-id')
        

class schedule(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100, default=None, null=True)
    last_name = models.CharField(max_length=100, default=None, null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(to=schedule_category, on_delete=models.CASCADE)

    objects = scheduleManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name