import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import GOOGLE_TOKEN_PATH, GOOGLE_CREDENTIALS_PATH
SCOPES = ["https://www.googleapis.com/auth/calendar"]

class GoogleCalendarClient:
    def __init__(self):
        self.credentials = None

    def auth(self):

        if os.path.exists(GOOGLE_TOKEN_PATH):
            print("[GOOGLE_CALENDAR_CLIENT] Found existing token file.")
            self.credentials = Credentials.from_authorized_user_file(GOOGLE_TOKEN_PATH, SCOPES)

        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                print("[GOOGLE_CALENDAR_CLIENT] Token expired. Refreshing...")
                self.credentials.refresh(Request())
            else:
                print("[GOOGLE_CALENDAR_CLIENT] No valid credentials. Starting OAuth flow...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    GOOGLE_CREDENTIALS_PATH, SCOPES
                )
                self.credentials = flow.run_local_server(port=0)

            print("[GOOGLE_CALENDAR_CLIENT] Saving credentials to token file.")
            with open(GOOGLE_TOKEN_PATH, "w") as token:
                token.write(self.credentials.to_json())
        else:
            print("[GOOGLE_CALENDAR_CLIENT] User already authenticated and token is valid.")

    def get_service(self):
        if not self.credentials:
            self.auth()

        try:
            service = build("calendar","v3", credentials=self.credentials)
            return service
        except:
            print("[GOOGLE_CALENDAR_CLIENT] Error when getting the service")
