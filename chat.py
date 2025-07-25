#Step 1: chatbot function
def simple_chatbot():
    print("Welcome to ChatBot! Type something to chat, or type 'bye' to disconnect/Exit.")

    while True: 
        u_input = input("You: ").lower() # Step 2: user input convert to lower case

#Step 3: predefine responses for specific inputs
        if u_input in ["hello", "hii", "hey", "hy era",]:
            print("Bot: Hi!")
        elif u_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif u_input in ["what's your name", "who are you", "your name"]:
            print("Bot: I'm a simple chatbot. You can call me Era.")
        elif u_input == "help":  
            print("Bot: How can I assist you?")
        elif u_input in ["exit", "quit", "bye"]:  # Step 4: if user type bye, exit the chat
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")
simple_chatbot()  # Step 5: return to chatbot
