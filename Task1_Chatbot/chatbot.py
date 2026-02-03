print(" Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hi there! How can I help you today? ")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: I am a rule-based chatbot created using Python.")

    elif user_input == "who created you":
        print("Bot: I was created by an intern as part of the CodSoft AI internship.")

    elif user_input == "what can you do":
        print("Bot: I can respond to simple questions using predefined rules.")

    elif user_input == "help":
        print("Bot: You can say hello, ask my name, or type bye to exit.")

    elif user_input == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs ")

    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence. It enables machines to think like humans.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language used in AI and web development.")

    elif user_input == "thank you":
        print("Bot: You're welcome! Happy to help ")

    elif user_input == "bye":
        print("Bot: Goodbye! Best of luck with your internship ")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try something else.")
