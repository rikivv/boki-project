from integrations.google_calendar.client import GoogleCalendarClient
from integrations.google_calendar import queries

client = GoogleCalendarClient()
service = client.get_service()

events = queries.calendar_get_next_n_events(service=service, n=1)

colors = service.colors().get().execute()

print(colors)