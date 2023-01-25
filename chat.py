import sys
try:
  import openai
except Exception as e:
  print("ERROR TRYING TO IMPORT openai")
  print("THE openai PYTHON LIBRARY MIGHT NOT BE INSTALLED")
  print("TRY RUNNING:")
  print("pip3 install openai")
  print("or")
  print("pip install openai")
  print("THEN TRY AGAIN.")
  sys.exit(-1)

key = None
try:
  with open('.env', 'r') as file:
    key = file.read().strip().split("=")[1].replace("'","")
except Exception as e:
  print("ERROR TRYING TO READ FILE .env: " + e)
  sys.exit(-1)

print('DEBUG key: [' + key + ']')   
openai.api_key = key

model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
