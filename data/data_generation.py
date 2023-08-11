import os
import openai


openai.api_version = ""
openai.api_key = ""

prompt_path = '/LRV-Instruction/prompts/positive_generation_prompt.txt'
with open(prompt_path) as f:
  contents = f.read()

response = openai.ChatCompletion.create(
            engine="gpt-4-32k-0314",  # engine = "deployment_name".
            messages=[{"role": "user", "content": contents}])

result = response['choices'][0]['message']['content']

output_path = './output_sample.txt'
file = open(output_path, "w")
L = []
L.append(result)
file.writelines(L)
file.close()
