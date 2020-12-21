def weekly_subject():
  return 'Coding Boot Camp - Tutorial Available'

def weekly_body():
  return """
Hi Everyone!
<br/>
I hope you had a great week! I have attached a link below to schedule another tutoring session if you wish. If you are already scheduled, please ignore this email.
<br/>
https://calendly.com/brandongatlin-81
<br/>
On the Calendly page, be sure you have the correct time zone selected in the section labeled "Times are in" 
If our availability doesn’t sync, let me know and I'll see if we can figure something out.
<br/>
<br/>
Maximum tutorial sessions per week - our week is Monday - Sunday.
<br/>
<ul>
    <li>Part-time (6 month boot camp) students are entitled to 1 session per week.</li>
    <li>Full-time (3 month boot camp) students are entitled to 2 sessions per week.</li>
</ul>
If you have any questions or none of the times available work for you please let me know and I would be happy to help.
<br/>
<br/>
If you would like to schedule regular, recurring sessions at the same day/time each week, just let me know by REPLY ALL and we can work it out.  This is particularly useful if you have a strict schedule so you won't have to compete for time on my calendar.
<br/>
<br/>
CC Central Support on all email by always using REPLY ALL.
<br/>
<br/>
Sincerely,
<br/>
Brandon Gatlin
"""

def confirmation_subject(day, month, date, time, tz):
  return f"Coding Boot Camp - Tutorial Confirmation {day} {month}/{date} @{time} {tz} Time"

def confirmation_body(student, day, month, date, time, tz, zoom):
  return f"""
Hi {student}!
<br/><br/>
Thank you for scheduling your session with me. I am looking forward to our session on <span style="color:red;">{day} {month}/{date} @{time} {tz} Time</span>.
<br/><br/>
If something comes up and the scheduled time will not work, let me know a minimum of 6 hours before the appointment time and we’ll figure something out.
<br/><br/>
This session will take place here: {zoom}
<br/><br/>
(If you have not used zoom before please join the meeting at least 15 minutes early because it may have you download and install some software.)
<br/><br/>
Again, all I need from you:
  <ul>
    <li>Be on Tutors & Students Slack 5 minutes before your time slot.</li>
    <li>Make sure your computer/mic/internet connection are working.</li>
    <li>Make sure your workspace is quiet and free from interruptions.</li>
    <li>At the end of the session, I will provide you with a link to a 2 minute evaluation form that you are required to complete.</li>
  </ul>
<br/>
Slack or email me with any questions.  I’m looking forward to our meeting!
<br/><br/>
Please Reply All to this email so that I know you have seen it.
<br/><br/>
(CC Central Support on all tutor email by always using REPLY ALL).
<br/><br/>
Sincerely,<br/>
Brandon Gatlin
"""

def get_day_name(day):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  return days[day]

def get_formatted_tz(tz):
  tzs = ['Central', 'Eastern', 'Pacific', 'Mountain']
  return tzs[tz]
  
  
  
  
  