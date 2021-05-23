from django.http import HttpResponse
from django.shortcuts import render

def eventCalendarView(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>eventView</h1>")

    myContext = {
        "meineVariable" : "das ist eine Context-Variable",
        "meineZahl" : 123,
        "meineListe" : [123, 234, 345]
    }

    return render(request, "events.html", myContext)


def addEventsView(request, *args, **kwargs):
    return render(request, "addevent.html", {})
    #return HttpResponse("<h1>addEventsView</h1>")
    

