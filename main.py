from Googler import Googler
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage
from Message import *
import os, sys
from dotenv import load_dotenv
from MySQLdb import _mysql

root = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{root}/.env')
env = os.getenv('env')
mysql_host = os.getenv('mysql_host')
mysql_db = os.getenv('mysql_db')
mysql_user = os.getenv('mysql_user')
mysql_password = os.getenv('mysql_password')
try:
  db=_mysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_password, db=mysql_db)
except Exception as e:
  print(e)
  sys.exit()

google_pw = os.getenv('apw')
me = 'brandongatlin.81@gmail.com'
alt_me = 'brandongatlin1981@me.com'
central_support = 'centraltutorsupport@bootcampspot.com'

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
  session_time = datetime.strptime(student[4], '%I:%M %p')
  session_time = session_time + timedelta(hours=tz_offset)
  session_time = session_time.strftime('%-I:%M %p')
  d = session_date.split('/')
  session_datetime = datetime(year=int(d[2]), month=int(d[0]), day=int(d[1]))
  if tomorrow.day == session_datetime.day:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
      email = EmailMessage()
      email['Subject'] = confirmation_subject(get_day_name(session_datetime.weekday()), session_datetime.month, session_datetime.day, session_time, get_formatted_tz(tz_offset))
      email['From'] = me
      if env == 'prod':
        email['To'] = student_email
      else:
        email['To'] = alt_me
      if env == 'prod':
        email['Cc'] = central_support
      email.set_content(confirmation_body(first_name, get_day_name(session_datetime.weekday()), session_datetime.month, session_datetime.day, session_time, get_formatted_tz(tz_offset), zoom_link), subtype='html')
      connection.starttls()
      connection.login(user=me, password=google_pw)
      connection.send_message(email)
      db.query(f"""
             INSERT INTO logs(recipients, type, time_stamp) VALUES(
               '{student_email}', 'confirmation', '{datetime.now()}' 
               );
             """)


# weekly spam email
weekday = datetime.now().weekday()
if weekday == 6:
  googler.scrape_current()
  current_students_emails = googler.current_students
  current_students_emails_formatted = [addr[0] for addr in current_students_emails]
  with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
    email = EmailMessage()
    email['Subject'] = weekly_subject()
    email['From'] = me
    if env == 'prod':
      email['To'] = ', '.join(current_students_emails_formatted)
    else:
      email['To'] = alt_me
    if env == 'prod':
      email['Cc'] = central_support
    email.set_content(weekly_body(), subtype='html')
    connection.starttls()
    connection.login(user=me, password=google_pw)
    connection.send_message(email)

db.close()