from django.db import models
from django.urls import reverse

class Event(models.Model):
    hashtag = models.CharField('Hashtag', max_length=200, default='#')                                                      # todo primary key, todo: check if # got deleted by the user
    organizer = models.CharField('Hashtag Organizer (optional)', max_length=100, null=True, blank=True, default='@')        # IG name, todo check if @ got deleted by the user
    dateStart = models.DateField('Date Start (optional)', blank=True, null=True)                                            # actual date-based events
    dateEnd = models.DateField('End Date (optional)', blank=True, null=True)                                                # start == end for day-only events
    FREQUENCY = [
        ('NONE', 'no'),
        ('WEEKLY', 'weekly'),
        ('MONTHLY', 'monthly'),
        ('ANNUALLY', 'annually'),
    ]
    recurring = models.CharField('Recurring?', max_length=10, null=True, blank=True, choices=FREQUENCY, default='NONE')    # todo: onclick show weekday field
    recurringDay = models.CharField('Recurring Week Day', max_length=100, null=True, blank=True, default='')      
    #isRecurringWeekly = models.BooleanField('Weekly?', null=True, blank=True, default=False)                     # e.g. teaparty
    #isRecurringMonthly = models.BooleanField('Monthly?', null=True, blank=True, default=False)                   # e.g. circle of exemplary plushies
    #isRecurringAnnually = models.BooleanField('Annually', null=True, blank=True, default=False)                  # e.g. earth day or may 4th

    #user = models.ForeignKey('auth.User') # todo user management: users can work with these events

    # todo isApproved-Feld

    def get_absolute_url(self):
        return reverse("events:event-details", kwargs={"eid": self.id})
        #return f"/events/{self.id}/details/"
