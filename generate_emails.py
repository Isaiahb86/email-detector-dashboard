import os
import random

malicious_snippets = [
    "Click here to reset your password now.",
    "Please run cmd.exe for more details.",
    "Visit http://badguy.com to claim your reward."
]

clean_snippets = [
    "Hope you're having a great day!",
    "Looking forward to our meeting next week.",
    "Don't forget to submit your report."
]

os.makedirs("emails", exist_ok=True)

for i in range(17):
    with open(f"emails/email_{i}.txt", "w") as f:
        if random.random() < 0.5:
            f.write(random.choice(malicious_snippets))
        else:
            f.write(random.choice(clean_snippets))

print("Fake emails generated.")
