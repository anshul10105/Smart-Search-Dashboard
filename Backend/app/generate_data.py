import os
import random

os.makedirs("Data/raw", exist_ok=True)

topics = [
"Artificial intelligence is transforming industries including healthcare and finance.",
"Football is the most popular sport in the world with millions of fans.",
"Machine learning helps computers learn patterns from data.",
"Climate change is affecting global weather patterns and ecosystems.",
"Data science combines statistics, programming, and domain knowledge.",
"Healthcare technology improves diagnosis and patient care.",
"Space exploration helps us understand the universe.",
"Cybersecurity protects systems from digital attacks."
]

for i in range(300):
    text = random.choice(topics)

    with open(f"Data/raw/doc_{i}.txt", "w") as f:
        f.write(text + f" Document number {i}")

print("300 varied documents created!")
