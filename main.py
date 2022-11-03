import openai

openai.api_key = "YOUR TOKEN HERE"


### function that uses the OpenAI API to call a request and generate a response from a prompt

def create_response(prompt):

  response = openai.Completion.create(
    engine="text-ada-001",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )


  ### response is a dictionary, so you have to use the "text" index to get the response from the AI
 
  response = (response.choices[0].text)[:-3]

  return response

while True:

  prompt = input(">>> ")

  ### if the word "bye" is within the prompt, the loop will break.
  if "bye" in prompt:
    print("Goodbye!")
    break

  else:

    ### uses the create_response function to generate a response

    response = create_response(prompt)

    print(response)
