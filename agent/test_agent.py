from agent.agent import EmailAgent


agent = EmailAgent()


print("=== TEST: Draft Reply ===")

result = agent.run(
    "برای ایمیل شماره 2 یک پاسخ محترمانه بنویس و بگو ساعت 10 برای من مناسب است."
)

print(result)