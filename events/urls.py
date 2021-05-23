from django.urls import path
from events.views import eventAllView, eventDetailView, eventAddView, eventUpdateView

app_name = "events"
urlpatterns = [
    path('', eventAllView, name="events"),
    path('add/', eventAddView, name="new-event"),
    path('<int:eid>/update/', eventUpdateView, name="update-event"),
    path('<int:eid>/details', eventDetailView, name="event-details"),
]
