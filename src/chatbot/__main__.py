import openai

from chatbot.console.application import Application
from chatbot.models.openai import OpenAIPrompt

if __name__ == "__main__":
    prompt_api = OpenAIPrompt()
    application = Application(prompt_api=prompt_api)
    try:
        result = application.run()
    except openai.error.AuthenticationError:
        print("Please set OPENAI_API_KEY environment variable")
    else:
        print(result)
