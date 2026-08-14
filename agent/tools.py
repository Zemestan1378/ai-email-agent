import json


def get_emails():

    with open(
        "data/emails.json",
        "r",
        encoding="utf-8"
    ) as file:

        emails = json.load(file)

    return emails