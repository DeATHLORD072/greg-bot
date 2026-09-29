import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="You are Greg, a personal assistant. Reply with exactly: Greg's brain is online 🤖"
)

print(response.text)
