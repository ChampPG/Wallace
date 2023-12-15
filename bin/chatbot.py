import requests
import json

# How to change API URL: https://github.com/jmorganca/ollama/issues/703

class ChatBot:
    def __init__(self, model="llama2"):
        """Initializes a chatbot instance.

        Args:
            model (str, optional): Name of the model to use for the chatbot. Defaults to "wallace".
        """
        # Initialize memory and load configurations for AI API
        self.memory_file = "data/configs/memory.json"
        self.memory = self.load_memory()
        # Load configurations for AI API
        json_data = json.load(open("data/configs/settings.json"))
        json_url = json_data["personal_ai_url"]
        self.url = f"http://{json_url}:11434"  # URL for the API
        # Set the model name
        self.model = model  # Model name
        self.memory_flag = True  # Flag to use memory-based response

    def load_memory(self):
        try:
            return json.load(open(self.memory_file))
        except:
            return []
        
    def clear_memory(self):
        self.memory = []
        json.dump([], open(self.memory_file, "w"))

    def ai_call(self, prompt):
        """Calls the AI API with the given prompt and returns the response.

        Args:
            prompt (str): Input text from user.
        """
        self.memory.append({"role": "user", "content": prompt})

        try:
            if self.memory_flag:
                message = self.handle_memory_based_response()
            else:
                message = self.handle_prompt_based_response(prompt)
        except Exception as e:
            print(f"Error during AI call: {e}")
            message = "Error during AI call."

        self.save_memory()
        return message

    def handle_memory_based_response(self):
        # Implementation for memory-based response
        # Documentation for the API: https://github.com/jmorganca/ollama/blob/main/docs/api.md#request-with-options
        url = self.url + "/api/chat"
        data = {
            "model": self.model,
            "messages": self.memory,
            "stream": False
        }
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise ValueError(f"Error from server: {response.status_code}")

        response_dict = response.json()
        response_text = response_dict.get("message")
        if not response_text:
            raise ValueError("Invalid response format from server.")
        response_text["role"] = "assistant"
        self.memory.append(response_text)
        return response_text["content"]
    
        raise NotImplementedError("Memory-based response handling is not implemented.")

    def handle_prompt_based_response(self, prompt):
        # Implementation for prompt-based response
        # Documentation for the API: https://github.com/jmorganca/ollama/blob/main/docs/api.md#request-with-options
        url = self.url + "/api/generate"
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise ValueError(f"Error from server: {response.status_code}")

        response_dict = response.json()
        response_text = response_dict.get("response")
        if not response_text:
            raise ValueError("Invalid response format from server.")

        self.memory.append({"role": "system", "content": response_text})
        return response_text

    def save_memory(self):
        try:
            json.dump(self.memory, open(self.memory_file, "w"))
        except Exception as e:
            print(f"Error saving memory: {e}")

# Usage example:
# bot = ChatBot()
# response = bot.ai_call("Hello Wallace, how are you doing today?")
