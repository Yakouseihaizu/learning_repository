import random

messages = ["It's certain",
            "It's decidely so",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful",]
if "It's certain" in messages:
    print(messages[random.randint(0,len(messages)-1)])