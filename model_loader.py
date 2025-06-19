from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class ModelLoader:
    def __init__(self, model_name="microsoft/phi-2"):
        print("Loading model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)
        print("Model loaded successfully.")
    
    def generate(self, prompt, max_tokens=200):
        response = self.pipeline(prompt, max_new_tokens=max_tokens, do_sample=True, temperature=0.7)
        return response[0]['generated_text'][len(prompt):].strip()
