class ChatMemory:
    def __init__(self, max_turns=5):
        self.memory = []
        self.max_turns = max_turns

    def add_user_message(self, message):
        self.memory.append({"role": "user", "content": message})
        self.trim()

    def add_assistant_message(self, message):
        self.memory.append({"role": "assistant", "content": message})
        self.trim()

    def trim(self):
        while len(self.memory) > self.max_turns * 2:  # user+assistant per turn
            self.memory.pop(0)

    def get_prompt(self):
        # Convert memory to a single text prompt
        prompt = ""
        for entry in self.memory:
            role = "User" if entry["role"] == "user" else "Assistant"
            prompt += f"{role}: {entry['content']}\n"
        prompt += "Assistant: "
        return prompt
