from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


prompt = """
Classify the sentiment

Text:
The customer service was slow but eventually sloved my issue.
# The customer service was good and helpful.

Return only:
Positive
Negative
Neutral
"""


response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)