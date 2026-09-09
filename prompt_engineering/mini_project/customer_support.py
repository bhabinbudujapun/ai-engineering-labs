import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def classify_intent(customer_message):

    prompt = f"""
    You are an expert customer support classifier.

    Classify customer messages into one of these categories:

    - Refund
    - Cancellation
    - Technical Issue
    - Account Issue
    - General Query

    Examples:

    Message: I want my money back.
    Category: Refund

    Message: Please cancel my subscription.
    Category: Cancellation

    Message: The app crashes whenever I open it.
    Category: Technical Issue

    Message: I cannot access my account.
    Category: Account Issue

    Message: What are your pricing plans?
    Category: General Query

    Classify the following message.

    Message:
    {customer_message}

    Return only the category.
    """

    chat = client.chats.create(
        model="gemini-3.6-flash",
    )

    response = chat.send_message(prompt)

    return response.text


if __name__ == "__main__":

    customer_message = input("Enter customer message: ")

    intent = classify_intent(customer_message)

    print("\nDetected Intent:")
    print(intent)