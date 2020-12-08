from Googler import Googler
from datetime import datetime
from datetime import timedelta
import smtplib
from email.message import EmailMessage
from Message import *

import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/github/pro/Automated-Email-App')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
pw = os.getenv("apw")

# daily check for conf email
googler = Googler()
googler.authenticate()
googler.scrape_future()
future_sessions_data = googler.future_session_data
tomorrow = datetime.now() + timedelta(days=1)
for student in future_sessions_data:
  first_name = student[0].split()[0]
  student_email = student[1]
  zoom_link = student[5]
  tz_offset = int(student[3])
  session_date = student[2]
  session_time = student[4]
  d = session_date.split('/')
  session_datetime = datetime(year=int(d[2]), month=int(d[0]), day=int(d[1]))
  if tomorrow.day == session_datetime.day:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
      email = EmailMessage()
      email['Subject'] = confirmation_subject(get_day_name(session_datetime.weekday()), session_datetime.month, session_datetime.day, session_time, get_formatted_tz(tz_offset))
      email['From'] = 'brandongatlin.81@gmail.com'
      # email['To'] = current_students_emails
      email['To'] = ['brandongatlin.81@gmail.com'] # testing
      email.set_content(confirmation_body(first_name, get_day_name(session_datetime.weekday()), session_datetime.month, session_datetime.day, session_time, get_formatted_tz(tz_offset), zoom_link), subtype='html')
      connection.starttls()
      connection.login(user='brandongatlin.81@gmail.com', password=pw)
      connection.send_message(email)

# weekly spam email
weekday = datetime.now().weekday()
# if weekday == 7:
if weekday > -1: # always true for testing
  googler.scrape_current()
  current_students_emails = googler.current_students
  with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
    email = EmailMessage()
    email['Subject'] = weekly_subject()
    email['From'] = 'brandongatlin.81@gmail.com'
    # email['To'] = current_students_emails
    email['To'] = ['brandongatlin.81@gmail.com'] # testing
    email.set_content(weekly_body(), subtype='html')
    connection.starttls()
    connection.login(user='brandongatlin.81@gmail.com', password=pw)
    connection.send_message(email)
