def display_reports(lost_items, found_items):
    print("\n----- All Reports -----")

    print("\nLost Items:")
    if len(lost_items) == 0:
        print("No lost item reports.")
    else:
        for lost in lost_items:
            print("\nReport ID:", lost["id"])
            print("Item:", lost["item"])
            print("Brand:", lost["brand"])
            print("Color:", lost["color"])
            print("Location:", lost["location"])
            print("Date:", lost["date"])
            print("Description:", lost["description"])

    print("\nFound Items:")
    if len(found_items) == 0:
        print("No found item reports.")
    else:
        for found in found_items:
            print("\nReport ID:", found["id"])
            print("Item:", found["item"])
            print("Brand:", found["brand"])
            print("Color:", found["color"])
            print("Location:", found["location"])
            print("Date:", found["date"])
            print("Description:", found["description"])

def display_match(match, item_match, description_match):
    lost = match["lost_item"]
    found = match["found_item"]

    print("\nPossible Match!")
    print("------------------------")
    print("Lost Report ID:", lost["id"])
    print("Found Report ID:", found["id"])
    print("Lost Item:", lost["item"])
    print("Found Item:", found["item"])
    print("Match Percentage:", match["score"], "%")

    if match["score"] >= 80:
        print("Match Status: Strong Match")
    elif match["score"] >= 65:
        print("Match Status: Good Match")
    else:
        print("Match Status: Possible Match")

    print("\nMatching Details:")

    if item_match(lost["item"], found["item"]):
        print("✓ Item")
    else:
        print("✗ Item")

    if lost["brand"].lower() == found["brand"].lower():
        print("✓ Brand")
    else:
        print("✗ Brand")

    if lost["color"].lower() == found["color"].lower():
        print("✓ Color")
    else:
        print("✗ Color")

    if lost["location"].lower() == found["location"].lower():
        print("✓ Location")
    else:
        print("✗ Location")

    if lost["date"] == found["date"]:
        print("✓ Date")
    else:
        print("✗ Date")

    if description_match(lost["description"], found["description"]):
        print("✓ Description")
    else:
        print("✗ Description")