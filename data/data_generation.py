import os
import openai


openai.api_version = ""
openai.api_key = ""

prompt_path = './prompt_sample.txt'
with open(prompt_path) as f:
  contents = f.read()

response = openai.ChatCompletion.create(
            engine="gpt-4-32k-0314",  # engine = "deployment_name".
            messages=[{"role": "user", "content": contents}])

result = response['choices'][0]['message']['content']

output_path = './output_sample.txt'
file = open(path32, "w")
L = []
L.append(result)
file.writelines(L)
file.close()
