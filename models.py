from django.conf import settings
from django.db import models
from django.urls import reverse

class PersonalInfo(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('PersonalInfo-detail', args=[str(self.id)])
    def __str__(self):
        return self.First_name
    def __str__(self):
        return self.Last_name
    def __str__(self):
        return self.Middle_name
    def __str__(self):
        return self.Address
    def __str__(self):
        return self.title
class Education(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    School_attended = models.CharField(max_length=100)
    Degree = models.CharField(max_length=100)
    GPA = models.FloatField(max_length=200)
    def get_absolute_url(self):
        return reverse('Education-detail', args=[str(self.id)])
    def __str__(self):
        return self.Degree
    def __str__(self):
        return self.GPA
    def __str__(self):
        return self.School_attended
    def __str__(self):
        return self.title
class SkillsSummary(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    summary = models.TextField(max_length=1000)
    def get_absolute_url(self):
        return reverse('SkillsSummary-detail', args=[str(self.id)])
    def __str__(self):
        return self.summary
    def __str__(self):
        return self.title
class JobHistory(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    summary = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse('JobHistory-detail', args=[str(self.id)])
    def __str__(self):
        return self.summary
    def __str__(self):
        return self.title
class Experience(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    Company = models.CharField(max_length=100)
    Duties = models.CharField(max_length=1000)
    summary = models.TextField(max_length=1000)
    Start_date = models.DateField(null=True, blank=True)
    End_Date = models.DateField('End', null=True, blank=True)
    def get_absolute_url(self):
        return reverse('Experience-detail', args=[str(self.id)])
    def __str__(self):
        return self.Company
    def __str__(self):
        return self.Duties
    def __str__(self):
        return self.summary
    def __str__(self):
        return self.title
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    Education = models.ForeignKey('Education', on_delete=models.CASCADE)
    

    
    
