from agent.agent import EmailAgent


agent = EmailAgent()

result = agent.run(
    "ایمیل‌های مربوط به سفارش را پیدا کن"
)

print(result)