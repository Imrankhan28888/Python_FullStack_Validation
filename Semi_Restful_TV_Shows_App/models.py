from django.db import models
from datetime import datetime


class ShowManager(models.Manager):

    def validate(self,form):
        errors = {}
        if len(form["title"]) < 2:
            errors["title"] = 'Title field should be at least 2 characters'
        title_with_same_name = Show.objects.filter(title=form['title'])
        if len(title_with_same_name) >0:
            errors["duplicate"] = 'Name already taken, pick another one'
        if len(form['network']) < 3:
            errors["network"] = 'Network field should be at least 3 characters'
        if form['description'] != '' and len(form['description']) < 10:
            errors['description'] = 'Description should be at least 10 characters'
        if datetime.strptime(form['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release Date should be in the past'
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()


