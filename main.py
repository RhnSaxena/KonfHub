import json
import config
from source.requestUtil import requestGet
from source.readable import createReadableDict
from source.replicas import createMap, findExactReplicas, findSimilar
from source.fileWriter import writeToJSONFile, writeToTXT


def driver():

    response = requestGet(config.link)

    readableData = createReadableDict(response)
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.readableFileName, extension="json"
        ),
        readableData,
    )
    writeToTXT(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.readableFileName, extension="txt"
        ),
        readableData,
    )
    print("The events have been printed in readable format.")

    eventDict = createMap(response)
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.eventsFileName, extension="json"
        ),
        eventDict,
    )
    print("The events have been printed.")

    duplicatesDict = findExactReplicas(eventDict)
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.exactDuplicatesFileName, extension="json"
        ),
        duplicatesDict,
    )
    print("The duplicates events have been printed.")

    similarDict = findSimilar(eventDict)
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.similarEventsFileName, extension="json"
        ),
        similarDict,
    )
    print("The similar events have been printed.")


driver()
