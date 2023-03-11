from chatbot.console.application import Application
from chatbot.models.openai import OpenAIPrompt

if __name__ == "__main__":
    prompt_api = OpenAIPrompt()
    application = Application(prompt_api=prompt_api)
    result = application.run()
    print(result)
