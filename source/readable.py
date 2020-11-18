def createReadableDict(data):
    dataDict = {}
    index = 0
    for category in ["paid", "free"]:
        for entry in data[category]:
            dataDict[index] = getReadableValue(entry)
            index = index + 1

    return dataDict


def getReadableValue(entry):
    return "{conferenceName}, {startDate}, {location}, {state}, {country}, {category}. {link}".format(
        conferenceName=entry["confName"],
        startDate=entry["confStartDate"],
        location=entry["city"],
        state=entry["state"],
        country=entry["country"],
        category=entry["entryType"],
        link=entry["confUrl"],
    )
