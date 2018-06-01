from django.db import models
from django.urls import reverse


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
        return reverse('manager:project', kwargs={'pk':self.pk})


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.FileField()
    salary = models.IntegerField()

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    projects = models.ManyToManyField(Project, blank=True)

    def get_absolute_url(self):
        return reverse('manager:employee', kwargs={'pk':self.pk})

