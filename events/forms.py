from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    #hashtag = forms.CharField(label="", widget=forms.TextInput(attrs={"id":"hashtagfield"}))

    
    # https://www.w3schools.com/jsref/event_onchange.asp <select onchange="myFunction()">

    class Meta:
        model = Event
        fields = ['hashtag', 'organizer', 'dateStart', 'dateEnd', 'recurring', 'recurringDay']



