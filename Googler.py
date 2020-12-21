import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Googler:
  def __init__(self):
      self.scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
      self.spreadsheet_id = '1wdALaet-18Be5vX4x2W1kR8UfkH3p8PAhLKxpopLkl8'
      self.current_students_scrape_range = 'Student Roster!D2:D100'
      self.future_sessions_scrape_range = 'Future Sessions!C2:H'
      self.creds = None
      self.future_session_data = []
      self.current_students = []
      
  def authenticate(self):
    creds = None
    if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', self.scopes)
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)
    self.creds = creds
    
  def scrape_future(self):
    service = build('sheets', 'v4', credentials=self.creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                range=self.future_sessions_scrape_range).execute()
    values = result.get('values', [])
    self.future_session_data = values
    
  def scrape_current(self):
    service = build('sheets', 'v4', credentials=self.creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                range=self.current_students_scrape_range).execute()
    values = result.get('values', [])
    self.current_students = values[1:]
      
