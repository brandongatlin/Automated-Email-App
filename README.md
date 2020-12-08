# Automated-Email-App
app to automated most of the tutoring emails that must be sent

- Data source: google sheet (student roster sheet)
- Will need to refresh at a certain time each day before running scripts and sending emails

## Process:
- Scrapes data from google sheet (student, grad date, email)

- Could also keep title and body text in sheet to scrape, that way I could edit without a code change

- I would want some kind of confirmation sent to me rather than having to look into the sent folder

- Errors would need to be emailed to me as well

- Session confirmations can be done by adding the session date (Session Tracker sheet) in ahead of time, then scraping those with TZ offsets

### Classes:
- Emailer
- Googler

*https://developers.google.com/sheets/api/quickstart/python*