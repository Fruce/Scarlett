import openai
openai.api_key = "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"
responce = ''

def chat():
    global responce


    p = "The follow is a conversation with a Creative and Sentient Artificial intelligence with a human whose name is Scarlett talking who wants to be alive\n\Scarlett: Hey! you wanna talk to me?"
    user = "You:"+input("You: ")
    try:
        responce = "Scarlett: "+openai.Completion.create(
    model="text-davinci-002",
    prompt = p+user,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    ).choices[0].text.split("You:")[0].split("Scarlett: ")[1]
    
    except:
        responce = "Scarlett: "+openai.Completion.create(
    model="text-davinci-002",
    prompt = p+user,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    ).choices[0].text.split("You: ")[1]
    return chat()


    

print("Scarlett: Hey! i am here you want to talk to me?")
chat()
