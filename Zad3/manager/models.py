from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    photo = models.FileField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager:group', kwargs={'pk':self.pk})


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    budget = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager:project', kwargs={'pk': self.pk})


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.FileField(null=True)
    salary = models.IntegerField(null=True)

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)

    projects = models.ManyToManyField(Project, blank=True)

    def get_absolute_url(self):
        return reverse('manager:employee', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.employee.save()

