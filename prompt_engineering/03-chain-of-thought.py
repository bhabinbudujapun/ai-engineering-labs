from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = """
Answer the question by reasoning step by step, then give the final answer.

Question:
A bakery had 48 croissants in the morning.
It sold 3/4 of them before noon and baked 18 more in the afternoon.
Then it sold 12 in the evening.
How many croissants are left at closing time?

Format your answer as:
Reasoning: <your step by step reasoning>
Answer: <a single number>
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
