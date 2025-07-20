#import openai

# ❗ Replace with your own API key securely (e.g., via environment variable)
openai.api_key = "sk-REPLACE_THIS_WITH_YOUR_REAL_KEY"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

if __name__ == "__main__":
    print("🤖 Chat with GPT-3.5 (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Exiting chat. Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")
