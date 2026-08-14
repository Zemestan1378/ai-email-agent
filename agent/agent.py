from google import genai

from config import GEMINI_API_KEY
from agent.tools import get_emails


class EmailAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def run(self, user_request):

        emails = get_emails()

        email_text = ""

        for email in emails:

            email_text += f"""
ID: {email["id"]}
From: {email["sender"]}
Subject: {email["subject"]}
Body: {email["body"]}
Date: {email["date"]}
"""

        prompt = f"""
You are an AI Email Management Agent.

User request:
{user_request}

Available emails:
{email_text}

Analyze the emails and complete the user's request.

Rules:
- Do not invent information.
- Identify important emails.
- Identify emails that require a reply.
- If a reply is requested, create a draft.
- Keep the answer concise.
"""

        interaction = self.client.interactions.create(
            model="gemini-3.5-flash",
            input=prompt
        )

        return interaction.output_text