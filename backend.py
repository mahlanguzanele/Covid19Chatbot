from openai import OpenAI
import os

class ChatBot:

    def __init__(self):
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    def get_response(self, user_input):
        try:
            prompt = f"Generate information about COVID-19 regulations: {user_input}"
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=3000,
                temperature=0.7
            )
            response_text = response.choices[0].text.strip().lower()

            # Check for specific user inputs and provide custom responses
            if "thank you" in user_input.lower():
                return "You're welcome!"

            if "bye" in user_input.lower():
                return "Goodbye! Stay safe."

            # Check if the response contains information about COVID-19
            if "covid" not in response_text:
                return "I'm sorry, I can only provide information about COVID-19 regulations."

            return response_text
        except Exception as e:
            print(f"Error while getting response: {e}")
            return None

if __name__ == "__main__":
    chatbot = ChatBot()
    user_input = input("You: ")

    while user_input.lower() != 'exit':
        response_g = chatbot.get_response(user_input)
        print(f"Bot: {response_g}")

        # Next user input
        user_input = input("You: ")
