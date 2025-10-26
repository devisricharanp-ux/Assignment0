from groq import Groq
import json

text = open("text.txt")
answer=open("answers.json","w")
key=open("key.env")

key_read=key.read()
data_text=text.read()  

client = Groq(api_key=key_read)
response =client.chat.completions.create(
  model = "llama-3.1-8b-instant",
   messages = [{"role":"user",
                 "content":data_text}]
)

y=json.dumps(response.choices[0].message.content)
answer.write(y)
print("Succesfully added to json file")
