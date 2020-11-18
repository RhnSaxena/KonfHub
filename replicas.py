def createMap(data):
    conferencesDict={}

    for category in ["paid", "free"]:
        for entry in data[category]:
            if entry["confStartDate"] in conferencesDict.keys():
                if entry["confEndDate"] in conferencesDict[entry["confStartDate"]].keys():
                    index = len(conferencesDict[entry["confStartDate"]][entry["confEndDate"]])
                    conferencesDict[entry["confStartDate"]][entry["confEndDate"]][index]=entry
                else:
                    entryDict={}
                    entryDict[0]=entry
                    conferencesDict[entry["confStartDate"]][entry["confEndDate"]]=entryDict
            else:
                entryDict, eventDict={}, {}
                eventDict[0]=entry
                entryDict[entry["confEndDate"]]=eventDict
                conferencesDict[entry["confStartDate"]]=entryDict

    return conferencesDict

    