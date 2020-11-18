def refine(data):
    for category in ["paid", "free"]:
        for entry in data[category]:
            print(
                "{conferenceName}, {startDate}, {location}, {state}, {country}, {category}. {link}".format(
                    conferenceName=entry["confName"],
                    startDate=entry["confStartDate"],
                    location=entry["city"],
                    state=entry["state"],
                    country=entry["country"],
                    category=entry["entryType"],
                    link=entry["confUrl"],
                )
            )
