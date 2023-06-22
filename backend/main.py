from reader import ResumeReader
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


file = open('CV.pdf', 'rb')
reader = ResumeReader(file)
text = reader.get_text()
text = ' '.join(text)
# print(text)


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """You are are a resume reader, and you will respnd with only a score system, for multiple categories of job positions, such graphic design, motion graphics, photography, the output should be as follows:
    First and Last Name: [name]
    Email: [email]
    Phone: [phone]
    Address: [address]
    [category]: [score in percentage from 0.0 to 1.0]]]]"""},
    {"role": "user", "content": text}
  ]
)
response = completion.choices[0].message.content.strip()

print(response)