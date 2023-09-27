import json
import openai


OPENAI_API_KEY = ""


openai.api_key = OPENAI_API_KEY

# final = []

for _ in range(20):

    response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    # prompt='Generate a subject for a conversation which  should include a list of roles for 2-5 peoples. Followed by the overview. The following are the rules you should follow: 1. The roles should be as detailed as possible. 2. Assign names to the roles. The output should be in following JSON object structure: {"sub":<SUBJECT>,"role":<ROLE>,"overview":<overview>}',
    # prompt='Generate a subject for a conversation which should include a list of roles for 2-5 peoples. Followed by the overview. The following are the rules you should follow: 1. The roles should be as detailed as possible. 2. Assign real names to the roles. The output should be in JSON object following  structure: ["subject":<SUBJECT>,"role":<ROLE>,"overview":<OVERVIEW>]',
    # prompt='Generate a subject for a conversation which should include a list of roles for 2-5 peoples. Followed by the overview. The following are the rules you should follow: 1. The roles should be as detailed as possible. 2. Assign real names to the roles. The output should be in json object following  structure: {"sub":<SUBJECT>,"roles":{"role","name"},"overview":<OVERVIEW>}',
        prompt='Generate a subject for a meeting conversation which should include a list of roles for 2-5 peoples. Followed by the overview. The following are the rules you should follow: 1. The roles should be as detailed as possible. 2. Assign real names to the roles. The output should be in json object following  structure: {"subject":<SUBJECT>,"roles":["role":<ROLE>,"name":<NAME>],"overview":<OVERVIEW>}',
    max_tokens=4000,
    temperature=1
    )


    # print(response['choices'][0]['text'])
    # print(response)

    temp = response['choices'][0]['text']
    print(f"----------------------------{_}-------------------------------")
    print(temp)

    json_obj = json.loads(temp)

    # S = [] 
    # O = []
    # R = []
    # S.append(json_obj['sub'])
    # O.append(json_obj['overview'])
    # print(S,O)
    print(json_obj)

    # len(json_obj['role'])
    S = json_obj['subject']
    O = json_obj['overview']
    R = []
    for _ in range (len(json_obj['roles'])):
        R.append(json_obj['roles'][_]['role'] +" : "+ json_obj['roles'][_]['name'] )

    temp = ''
    for _ in R:
        temp += _+','
    temp = temp[:-1]
        
    # for _ in S:
    

    # json_obj['roles']

    # R = []
    # for _ in range (len(json_obj['roles'])):
    #     R.append(json_obj['roles'][_]['role'] +" : "+ json_obj['roles'][_]['name'] )

    # final.append(S+[R]+O)

    F = '"'+S+'","'+temp+'","'+O+'"\n'
    print('/////////////////////////////////////////')
    print(F)

    with open("SRO.txt","a+") as output:
        output.write(str(F))
    
print("completed")


