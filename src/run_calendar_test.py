from integrations.google_calendar.client import GoogleCalendarClient
from integrations.google_calendar import queries
from datetime import datetime


# client = GoogleCalendarClient()
# service = client.get_service()

# events = queries.calendar_get_next_n_events(n=5)

# colors = service.colors().get().execute()

# queries.calendar_create_event("oi", 123, 123, 123)

# #print(colors)

input = "/dsakfjsfaf"

print(f"Today is {datetime.now().astimezone().strftime('%A, %B %d, %Y at %H:%M (%z)')}")