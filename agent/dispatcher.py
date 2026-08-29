from agent.tools import (
    search_emails,
    search_emails_semantic,
    get_email,
    draft_reply,
)


def execute_tool(tool_name: str, arguments: dict):

    if tool_name == "search_emails":
        return search_emails(
            arguments.get("query", "")
        )

    if tool_name == "search_emails_semantic":
        return search_emails_semantic(
            arguments.get("query", "")
        )

    if tool_name == "get_email":
        email_id = arguments.get("email_id")

        if email_id is None:
            return {
                "error": "email_id is required"
            }

        return get_email(int(email_id))

    if tool_name == "draft_reply":
        email_id = arguments.get("email_id")
        instruction = arguments.get(
            "instruction",
            ""
        )

        if email_id is None:
            return {
                "error": "email_id is required"
            }

        return draft_reply(
            int(email_id),
            instruction
        )

    return {
        "error": f"Unknown tool: {tool_name}"
    }