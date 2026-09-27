from storage import load_data, save_data
from validation import get_non_empty_input, get_date_input
from matching import item_match, description_match, calculate_match
from reports import display_reports, display_match

print("========================================")
print("     CAMPUS LOST & FOUND MATCHER")
print("========================================")

lost_items, found_items = load_data()

if len(lost_items) == 0:
    lost_id = 1
else:
    lost_id = max(item["id"] for item in lost_items) + 1


if len(found_items) == 0:
    found_id = 1
else:
    found_id = max(item["id"] for item in found_items) + 1

while True:
    print()
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. Find Matches")
    print("4. View Reports")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if not choice.isdigit():
        print("Please enter a number between 1 and 5")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        print("\n----- Report Lost Item -----")

        item = get_non_empty_input("Enter item name: ")
        brand = get_non_empty_input("Enter brand: ")
        color = get_non_empty_input("Enter color: ")
        location = get_non_empty_input("Where was it lost? ")
        date = get_date_input("Enter date (DD/MM/YYYY): ")
        description = get_non_empty_input("Enter description: ")

        lost_item = {
            "id": lost_id,
            "item": item,
            "brand": brand,
            "color": color,
            "location": location,
            "date": date,
            "description": description
        }

        lost_items.append(lost_item)
        save_data(lost_items, found_items)
        lost_id += 1

        print("\n----- Lost Item Report -----")
        print("Report ID:", lost_item["id"])
        print("Item:", item)
        print("Brand:", brand)
        print("Color:", color)
        print("Location:", location)
        print("Date:", date)
        print("Description:", description)

    elif choice == 2:
        print("\n----- Report Found Item -----")

        item = get_non_empty_input("Enter item name: ")
        brand = get_non_empty_input("Enter brand: ")
        color = get_non_empty_input("Enter color: ")
        location = get_non_empty_input("Where was it found? ")
        date = get_date_input("Enter date (DD/MM/YYYY): ")
        description = get_non_empty_input("Enter description: ")

        found_item = {
            "id": found_id,
            "item": item,
            "brand": brand,
            "color": color,
            "location": location,
            "date": date,
            "description": description
        }

        found_items.append(found_item)
        save_data(lost_items, found_items)
        found_id += 1

        print("\n----- Found Item Report -----")
        print("Report ID:", found_item["id"])
        print("Item:", item)
        print("Brand:", brand)
        print("Color:", color)
        print("Location:", location)
        print("Date:", date)
        print("Description:", description)

    elif choice == 3:
        print("\n----- Find Matches -----")

        if len(lost_items) == 0 or len(found_items) == 0:
            print("Not enough reports to find a match.")
        else:
            matches = []

            for lost_item in lost_items:
                found_match = False

                for found_item in found_items:
                    score = calculate_match(lost_item, found_item)

                    if score >= 50:
                        matches.append({
                            "lost_item": lost_item,
                            "found_item": found_item,
                            "score": score
                        })
                        found_match = True

                if found_match == False:
                    print("No match found for Lost Report ID:", lost_item["id"],
                          "(", lost_item["item"], ")")

            if len(matches) == 0:
                print("No possible matches found.")
            else:
                matches.sort(key=lambda match: match["score"], reverse=True)

                for match in matches:
                    display_match(match, item_match, description_match)

    elif choice == 4:
        display_reports(lost_items, found_items)

    
    elif choice == 5:
        print("Thank you for using Campus Lost & Found Matcher!")
        print("Your reports have been saved successfully. See you later!")
        break