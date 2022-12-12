import openai

completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt="hello world",
    temperature=0.5,
)

for choice in completion.choices:
    print(choice.text)
