
import analytics


def process_expenses(rawPrices):
    return [analytics.add_percent(p, 15) for p in rawPrices]


def analyze_scores(n):
    scores = []
    for i in range(n):
        scores.append(float(input(f"Enter score #{i + 1}: ")))

    highest = analytics.find_max(scores)
    avg = analytics.average(scores)
    return highest, avg


def sanitize_usernames(usernames):
    return [analytics.to_lower(analytics.remove_spaces(name)) for name in usernames]


def identify_outliers(values):
    return analytics.filter_over(values, 100)


def search_and_report(items):
    cleaned = [analytics.to_lower(analytics.remove_spaces(x)) for x in items]

    target = analytics.to_lower(analytics.remove_spaces(input("Item to search for: ")))

    if analytics.is_sorted(cleaned):
        return analytics.binary_search(cleaned, target)
    return analytics.linear_search(cleaned, target)

