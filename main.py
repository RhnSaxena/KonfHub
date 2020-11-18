import json
import config
from source.requestUtil import requestGet
from source.readable import createReadableDict
from source.replicas import createDict, findExactReplicas, findSimilar
from source.fileWriter import writeToJSONFile, writeToTXT


def driver():

    # Perform the GET operation on the link
    # and receive response
    response = requestGet(config.link)

    # Create a dict in readable format.
    readableData = createReadableDict(response)
    # Write the readable dict to .json file
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.readableFileName, extension="json"
        ),
        readableData,
    )
    # Write the readable dict to .txt file
    writeToTXT(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.readableFileName, extension="txt"
        ),
        readableData,
    )
    print("The events have been printed in readable format.")

    # Create Dictionary for the events,
    # and write it to .json file
    eventDict = createDict(response)
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.eventsFileName, extension="json"
        ),
        eventDict,
    )
    print("The events have been printed.")

    # Find duplicates events,
    # and write it to .json file
    duplicatesDict = findExactReplicas(eventDict)
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.exactDuplicatesFileName, extension="json"
        ),
        duplicatesDict,
    )
    print("The duplicates events have been printed.")

    # Find similar events,
    # and write it to .json file
    similarDict = findSimilar(eventDict)
    writeToJSONFile(
        "./{folder}/{file}.{extension}".format(
            folder=config.folder, file=config.similarEventsFileName, extension="json"
        ),
        similarDict,
    )
    print("The similar events have been printed.")


driver()
