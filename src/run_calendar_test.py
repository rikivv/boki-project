from integrations.google_calendar.client import GoogleCalendarClient
from integrations.google_calendar import queries


events = queries.calendar_get_next_n_events(n=2)

for event in events:
    print(event["summary"])