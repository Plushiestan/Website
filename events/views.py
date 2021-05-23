from django.shortcuts import render, get_object_or_404
from .models import Event
from .forms import EventForm


def eventAllView(request):
    queryset = Event.objects.all()
    #queryset = Event.objects.filter(id__gt=3)
    context = {
        "objectList" : queryset
    }
    return render(request, "event/all.html", context)




def eventDetailView(request, eid):
    #obj = Event.objects.get(id=eid)
    obj = get_object_or_404(Event, id=eid)
    context = {
        "data" : obj
    }
    return render(request, "event/detail.html", context)




def eventAddView(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        cht = cleanHashtag(form)
        form.fields['hashtag'] = cht
        print(form.fields['hashtag'])
        form.save() # doesn't save the hashtag prefix although printed, todo
        form = EventForm() # clear form

    context = {
        "form" : form
    }
    return render(request, "event/create.html", context)





def eventUpdateView(request, eid):
    #if request.user == "fluffysmom": # todo check user
        print(request.user)
        obj = get_object_or_404(Event, id=eid)
        form = EventForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save() 
            form = EventForm() 

        context = {
            "form" : form
        }
    
        return render(request, "event/update.html", context)
   # else:
        #return render(request, "event/detail.html", context)










# todo use cleanHashtag before saving to database
# https://micropyramid.com/blog/django-forms-basics/
# https://www.geeksforgeeks.org/overriding-the-save-method-django-models/
def save(self, *args, **kwargs):
    self.hashtag = cleanHashtag(self)
    super(EventModel, self).save(*args, **kwargs)



def cleanHashtag(self, *args, **kwargs):
    hashtag = self.cleaned_data.get("hashtag")
    if hashtag.startswith("##"):
        return hashtag[1:]
    elif hashtag.startswith("#"):
        return hashtag
    else:
        return "#"+hashtag


def cleanOrganizer(self, *args, **kwargs):
    organizer = self.cleaned_data.get("organizer")
    if organizer.startswith("@@"):
        return organizer[1:]
    elif organizer.startswith("@"):
        return organizer
    else:
        return "@"+organizer
