import json


file = open('input_data.txt','r')
line = file.readlines()
for i in range(0,len(line)):
    first = line[i]

    # print("---------------------line---------------------")

    # print(first)

    json_obj = json.loads(first)
    sample = json_obj.replace('\n', '')

    start_idx = sample.find("```")

    # Find the last occurrence of "```"
    end_idx = sample.rfind("```")

    # Check if both markers are found
    if start_idx != -1 and end_idx != -1:
        # Extract the sample between the markers
        temp = sample[start_idx + 3:end_idx]
        final_data = temp[4:]
        final_data.replace("'",'"')
        final_data.replace('"s',"'s")
        # Print the result
        # print("---------------------Data---------------------")

        # print(final_data)

    data = json.loads(final_data)

    if len(data) == 1:

        trans ="{'data': "+ str(data[0]["data"])+"}"
        res = "{'response': "+str(data[0]['response'])+"}"
    else:
        trans = data[0]
        res = data[1]


    # with open("full_filtered_data.txt",'+a') as f:
    #     f.write(str(trans))
    #     f.write(',')
    #     f.write(str(res))
    #     f.write('\n')

    with open("filtered_transcript.txt",'+a') as t:
        t.write(str(trans))
        t.write('\n')
    with open("filtered_response.txt",'+a') as r:
        r.write(str(res))
        r.write('\n')
    # print("================",data,"================",res,"================")
    # print(data[0])
    print(f'{i+1} completed')
    # print(len(data))

print('DONE !!!')