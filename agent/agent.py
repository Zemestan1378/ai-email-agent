import json

import ollama

from agent.dispatcher import execute_tool


MODEL = "qwen2.5:3b"


class EmailAgent:

    def run(self, user_request: str):

        messages = [
            {
                "role": "system",
                "content": """
You are an AI email assistant.

Available tools:

1. search_emails(query)
Search emails using keyword matching.

2. search_emails_semantic(query)
Search emails using semantic/vector search.

3. get_email(email_id)
Get one specific email.

4. draft_reply(email_id, instruction)
Create a reply draft for a specific email.
This tool DOES NOT send emails.

When a tool is needed, respond ONLY with valid JSON.

Keyword search:

{
    "tool": "search_emails",
    "arguments": {
        "query": "..."
    }
}

Semantic search:

{
    "tool": "search_emails_semantic",
    "arguments": {
        "query": "..."
    }
}

Get email:

{
    "tool": "get_email",
    "arguments": {
        "email_id": 1
    }
}

Draft reply:

{
    "tool": "draft_reply",
    "arguments": {
        "email_id": 1,
        "instruction": "Write a polite reply."
    }
}

IMPORTANT:
- Never invent email information.
- Never invent tool results.
- Never send an email.
- draft_reply only prepares information for a reply.
- Final answers must be based only on tool results.
- Answer in Persian.
"""
            },
            {
                "role": "user",
                "content": user_request
            }
        ]

        for step in range(3):

            response = ollama.chat(
                model=MODEL,
                messages=messages
            )

            content = response["message"]["content"].strip()

            try:
                decision = json.loads(content)

            except json.JSONDecodeError:
                return content

            tool_name = decision.get("tool")

            if not tool_name:
                return content

            arguments = decision.get(
                "arguments",
                {}
            )

            tool_result = execute_tool(
                tool_name,
                arguments
            )

            messages.append(
                {
                    "role": "assistant",
                    "content": content
                }
            )

            messages.append(
                {
                    "role": "user",
                    "content": (
                        "TOOL RESULT:\n"
                        + json.dumps(
                            tool_result,
                            ensure_ascii=False,
                            indent=2
                        )
                        + "\n\n"
                        "Now answer the original user request "
                        "using only the tool result."
                    )
                }
            )

        return "Agent به حداکثر تعداد مراحل رسید."