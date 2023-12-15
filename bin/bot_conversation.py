from chatbot import ChatBot

def chat_between_bots(bot1, bot2, initial_prompt):
    """
    Facilitates a continuous conversation between two chatbot instances.

    Args:
    bot1 (ChatBot): The first chatbot instance.
    bot2 (ChatBot): The second chatbot instance.
    initial_prompt (str): The initial prompt to start the conversation.
    """
    print("Starting conversation:")
    print(f"Bot 1: {initial_prompt}")
    
    current_prompt = initial_prompt
    turn = 0

    while True:
        if turn % 2 == 0:
            # Bot 1's turn
            current_prompt = bot1.ai_call(current_prompt)
            print(f"Bot 2: {current_prompt}")
        else:
            # Bot 2's turn
            current_prompt = bot2.ai_call(current_prompt)
            print(f"Bot 1: {current_prompt}")
        
        turn += 1

if __name__ == "__main__":
    # Create two chatbot instances
    bot1 = ChatBot("llama2-uncensored")  # Use the "wallace" model for bot 1
    bot2 = ChatBot("wizard-vicuna-uncensored")  # Use the "wallace" model for bot 2

    # Start a continuous conversation with an initial prompt
    initial_prompt = "Hello, how are you?"
    chat_between_bots(bot1, bot2, initial_prompt)