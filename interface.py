from model_loader import ModelLoader
from chat_memory import ChatMemory   


def main():
    #model_name = "openchat/openchat-3.5-0106"
    model_loader = ModelLoader(model_name="openchat/openchat-3.5-0106")
    memory = ChatMemory(max_turns=5)
    
    print("Chatbot started. Type /exit to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "/exit":
            print("Goodbye!")
            break
        
        memory.add_user_message(user_input)
        prompt = memory.get_prompt()
        reply = model_loader.generate(prompt)
        print("Assistant:", reply)
        memory.add_assistant_message(reply)

if __name__ == "__main__":
    main()
