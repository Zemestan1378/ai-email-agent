from agent.tools import search_emails


results = search_emails("سفارش")

for email in results:
    print(email)