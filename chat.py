import openai
import os
key ="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"
openai.api_key = key

response = openai.Completion.create(model="text-davinci-003", prompt="Generate an excuse", temperature=1.5, max_tokens=50)
choices=response["choices"]
choices_dict=choices[0]
print(choices_dict["text"])