def main():
    print("Chatbot started. Type /exit to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break
        elif user_input.lower()=="history":
            print(memory.history())
            continue
        
        memory.add_user_message(user_input)
        prompt = memory.get_prompt()
        reply = model_loader.generate(prompt)
      
        print("Assistant:", reply)
        memory.add_assistant_message(reply)
 
if __name__ == "__main__":
    main()
