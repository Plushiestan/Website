from django.db import models

class Birthday(models.Model):
    instagramName = models.CharField('Instagram Account Name', max_length=100, null=False, default='@')
    plushieName = models.CharField('Name of the Plushie', max_length=100, null=False)
    date = models.DateField('Birthday', null=False) 
    #user = models.ForeignKey('auth.User') # todo user management: users can work with these birthdays, e.g. ignore or set reminder
    
