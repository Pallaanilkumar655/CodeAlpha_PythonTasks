while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you 😊")
    elif user == "how are you":
        print("Bot: I'm doing great! How about you?")
    elif user == "your name":
        print("Bot: I'm a simple Python chatbot.")
    elif user == "help":
        print("Bot: You can say hello, how are you, or bye.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day 👋")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")