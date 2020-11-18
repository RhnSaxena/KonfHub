def createMap(data):
    conferencesDict = {}

    for category in ["paid", "free"]:
        for entry in data[category]:
            if entry["confStartDate"] in conferencesDict.keys():
                if (
                    entry["confEndDate"]
                    in conferencesDict[entry["confStartDate"]].keys()
                ):
                    index = len(
                        conferencesDict[entry["confStartDate"]][entry["confEndDate"]]
                    )
                    conferencesDict[entry["confStartDate"]][entry["confEndDate"]][
                        index
                    ] = entry
                else:
                    entryDict = {}
                    entryDict[0] = entry
                    conferencesDict[entry["confStartDate"]][
                        entry["confEndDate"]
                    ] = entryDict
            else:
                entryDict, eventDict = {}, {}
                eventDict[0] = entry
                entryDict[entry["confEndDate"]] = eventDict
                conferencesDict[entry["confStartDate"]] = entryDict

    return conferencesDict


def findExactReplicas(data):

    replicasDict = {}

    for startDate in data:
        for endDate in data[startDate]:
            noOfEvents = len(data[startDate][endDate])
            if noOfEvents > 1:
                for indexEvent1 in range(0, noOfEvents - 1):
                    event1 = data[startDate][endDate][indexEvent1]
                    for indexEvent2 in range(indexEvent1 + 1, noOfEvents):
                        event2 = data[startDate][endDate][indexEvent2]
                        equalFlag = True
                        for key in event1.keys():
                            if event1[key] != event2[key]:
                                equalFlag = False
                                break
                        if equalFlag:
                            replicasDict[len(replicasDict)] = event1
                            break

    return replicasDict


def findSimilar(data):

    similarDict = {}

    for startDate in data:
        for endDate in data[startDate]:
            noOfEvents = len(data[startDate][endDate])
            if noOfEvents > 1:
                for indexEvent1 in range(0, noOfEvents - 1):
                    event1 = data[startDate][endDate][indexEvent1]
                    for indexEvent2 in range(indexEvent1 + 1, noOfEvents):
                        event2 = data[startDate][endDate][indexEvent2]
                        equalFlag = True
                        for key in event1.keys():
                            if key not in ["confName", "searchTerms", "venue"]:
                                if event1[key] != event2[key]:
                                    equalFlag = False
                                    break
                        if equalFlag:
                            similarDict[len(similarDict)] = event1
                            break

    return similarDict
