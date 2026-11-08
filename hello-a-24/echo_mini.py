from datetime import datetime


rules = {
    "name": "من Echo-mini هستم، ساخته‌ی نهال",
    "hello": "Hello! How can I help you?😎",
    "time": lambda: datetime.now().strftime("%H:%M"),
    "add": lambda a, b: a + b,
    "bye": "Bye! See you later 😊"
}


# Run Agent 
print(rules["name"])

while True:
    command = input("You: ").lower().strip()

    if command == "hello":
        print("Echo-mini:", rules["hello"])

    elif command == "time":
        print("Echo-mini:", rules["time"]())

    elif command == "add":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print("Echo-mini:", rules["add"](a, b))

    elif command == "bye":
        print("Echo-mini:", rules["bye"])
        break

    else:
        print("Echo-mini: I don't understand that command.")

 