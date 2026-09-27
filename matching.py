def description_match(description1, description2):
    stop_words = {"the", "a", "an", "with", "and", "in", "on", "of", "to", "having"}

    words1 = set(description1.lower().split())
    words2 = set(description2.lower().split())

    words1 = words1 - stop_words
    words2 = words2 - stop_words

    common_words = words1.intersection(words2)

    if len(common_words) >= 2:
        return True
    else:
        return False

def item_match(item1, item2):
    item1 = item1.lower().split()
    item2 = item2.lower().split()

    words1 = set(item1)
    words2 = set(item2)

    if words1 == words2:
        return 30

    common_words = words1.intersection(words2)

    if len(common_words) >= 1:
        return 15

    return 0

def calculate_match(lost_item, found_item):
    score = 0

    score += item_match(lost_item["item"], found_item["item"])

    if lost_item["brand"].lower() == found_item["brand"].lower():
        score += 15

    if lost_item["color"].lower() == found_item["color"].lower():
        score += 15

    if lost_item["location"].lower() == found_item["location"].lower():
        score += 15

    if lost_item["date"] == found_item["date"]:
        score += 10

    if description_match(lost_item["description"], found_item["description"]):
        score += 15

    return score