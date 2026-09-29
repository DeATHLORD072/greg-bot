import os
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from icalendar import Calendar
import recurring_ical_events

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
ICAL_URL = os.environ["GOOGLE_CALENDAR_ICAL_URL"]

TZ = ZoneInfo("Asia/Kolkata")

response = requests.get(ICAL_URL)
response.raise_for_status()

calendar = Calendar.from_ical(response.text)

now = datetime.now(TZ)
start = now.replace(hour=0, minute=0, second=0, microsecond=0)
end = start + timedelta(days=1)

events = recurring_ical_events.of(calendar).between(start, end)

events.sort(key=lambda event: event.decoded("DTSTART"))

message = "📅 Good morning! Here's your schedule for today:\n\n"

if not events:
    message += "✨ Nothing scheduled today. You're free!"

else:
    for event in events:
        title = str(event.get("SUMMARY", "Untitled"))
        dt = event.decoded("DTSTART")

        if isinstance(dt, datetime):
            dt = dt.astimezone(TZ)
            time = dt.strftime("%I:%M %p").lstrip("0")
            message += f"🕐 {time} • {title}\n"
        else:
            message += f"📌 All day • {title}\n"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)
