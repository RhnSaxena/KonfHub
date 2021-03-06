import json

# Function that accept filename and data as
#  a dictionary and write it to .json file.
def writeToJSONFile(fileName, dictData):
    with open(fileName, "w", encoding="utf-8") as f:
        jsonText = json.dumps(dictData)
        f.write(jsonText)
    f.close()


# Function that accept filename and data as
#  a dictionary and write it to .txt file.
def writeToTXT(fileName, dictData):
    with open(fileName, "w", encoding="utf-8") as f:
        for index in dictData:
            f.write("{index}. {data}\n".format(index=index + 1, data=dictData[index]))
    f.close()
