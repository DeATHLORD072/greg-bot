import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.responses.create(
    model="gpt-5.6-luna",
    input="You are Greg, a personal assistant. Reply with exactly: Greg's brain is online 🤖"
)

print(response.output_text)
