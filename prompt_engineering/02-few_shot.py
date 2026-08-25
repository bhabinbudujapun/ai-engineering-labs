from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = """
Review: "This movie was a waste of time."
Sentiment: Negative
Review: "I couldn't stop laughing throughout the film!"
Sentiment: Positive
Review: "The special effects were amazing, but the plot was confusing."
Sentiment:
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