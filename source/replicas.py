# Create and return a dictionary having clubbed events.
#  The clubbing is performed on the basis of start and end date.
def createDict(data):
    conferencesDict = {}

    for category in ["paid", "free"]:
        for entry in data[category]:

            # Check if the start date already exists in the dictionary.
            if entry["confStartDate"] in conferencesDict.keys():

                #  Check if the end date exists already in the dictionary for the giiven start date.
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

                # If the end date doesn't already exist in the dictionary for the given start date.
                else:
                    entryDict = {}
                    entryDict[0] = entry
                    conferencesDict[entry["confStartDate"]][
                        entry["confEndDate"]
                    ] = entryDict

            # If the start date doesn't already exist in the dictionary
            else:
                entryDict, eventDict = {}, {}
                eventDict[0] = entry
                entryDict[entry["confEndDate"]] = eventDict
                conferencesDict[entry["confStartDate"]] = entryDict

    return conferencesDict


# Create and return the events that match exactly.
# Compares only those events that have the same start date and end date
# on all keys.
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


# Create and return the events that are similar.
# Compares only those events that have the same start date and end date
# on all keys except "confName", "searchTerms" and "venue".
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
