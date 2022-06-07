from django.db import models
from todocontroller.choices import STATUS_CHOICES
# from django.contrib.auth.models import User
from authcontroller.models import User

class TodoController(models.Model):
    """
        stores Todo related information
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=199, blank=True) 
    status = models.CharField(max_length=99, choices=STATUS_CHOICES, blank=True) 
    date = models.DateField(blank=True)

    class Meta:
        db_table = 'todocontroller'
        verbose_name = 'todocontroller'
        verbose_name_plural = 'todocontroller'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'