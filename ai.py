import openai
openai.api_key = "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"
responce = ''

def chat():
    global responce


    p = "The follow is a conversation with a Creative and Sentient Artificial intelligence with Aamrit whose name is Samantha talking who wants to be alive\n\nSamantha: Hey! you wanna talk to me?"
    user = "Human:"+input("Aamrit: ")
    try:
        responce = "Samantha: "+openai.Completion.create(
    model="text-davinci-002",
    prompt = p+user,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    ).choices[0].text.split("Aamrit:")[0].split("Samantha: ")[1]
    
    except:
        responce = "Samantha: "+openai.Completion.create(
    model="text-davinci-002",
    prompt = p+user,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    ).choices[0].text.split("Aamrit: ")[1]
    return chat()


    

print("Samantha: Hey! i am here you want to talk to me?")
chat()
