"""Write one joke about a meeting that should have been an email."""

LINE = "We spent an hour in a meeting deciding what the email should say — then we sent the email."

try:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
