#CREATING PROMPTS FROM CSV 
#COMBING SUBJECT, ROLES, OVERVIEW 

import pandas as pd


SRO_FILE_PATH_EXCEL = ""

df = pd.read_excel(SRO_FILE_PATH_EXCEL)

for i in range(0,len(df)):
    sub = df['Subject'][i]
    role = df["Roles"][i]
    over = df["Overview"][i]

    # prompt = """
    # Generate a Transcript for a conversation. The conversation subject is delimited by ``` and pesron roles is delimited by !!! followed by the overview which is delimited by ###.""" +  f" ```{sub}``` !!!{role}!!! ###{over}###"+' The following are the rules should be followed: 1. Trancript should be very details & precise. 2. Transcript should include wide range of problems, bugs and issues. 3. Must include various ACTION ITEMS related to conversation topic. 4. Has to be intresting. 5. Should be polite & realistic. 6. Transcript should have various names. 7. Feel free to add anything to make conversation flawless. 8. Do not write whole paragraph. Split it into short and meaningful sentences. 9. It should feel like real-time conversation. 10. Interuption should be there to make it look like real conversation. 11. Remove their designation for the roles filed. The output should be in json object following  structure: {"data":[["name","content"],["name","content"]]}'


    update_prompt =""" Generate a Transcript and response for a conversation. The conversation subject is delimited by ``` and pesron roles is delimited by !!! followed by the overview which is delimited by ###.""" +  f" ```{sub}``` !!!{role}!!! ###{over}###"+ 'The following are the rules should be followed: 1. Trancript should be very details & precise. 2. Transcript should include wide range of problems, bugs and issues. 3. Must include various ACTION ITEMS related to conversation topic. 4. Has to be intresting. 5. Should be polite & realistic. 6. Transcript should have various names. 7. Feel free to add anything to make conversation flawless. 8. Do not write whole paragraph. Split it into short and meaningful sentences. 9. It should feel like real-time conversation. 10. Interuption should be there to make it look like real conversation. 11. Remove their designation for the roles filed. The output should be in json object following  structure: [{"data":[["name","content"],["name","content"]]}, {"response":[[<TITLE>],[<SUMMARY>],[<ACTIONITEM>],[<ROADBLOCK>]]}].'


    with open("prompts.txt", 'a+') as f:
        f.write(update_prompt)
        f.write("\n")
