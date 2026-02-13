import analytics

def process_expenses(rawPrices):
    return [analytics.add_percent(p, 15) for p in rawPrices]

def analyze_scores(n):
    scores = []
    for _ in range(n):
        scores.append(float(input("")))
    high = analytics.find_max(scores)
    avg = analytics.average(scores)
    return high, avg

def sanitize_usernames(usernames):
    return [analytics.to_lower(analytics.remove_spaces(s)) for s in usernames]

def identify_outliers(values):
    return analytics.filter_over(values, 100)

def search_and_report(items):
    cleaned = sanitize_usernames(items)
    target = analytics.to_lower(analytics.remove_spaces(input("")))

    if analytics.is_sorted(cleaned):
        return analytics.binary_search(cleaned, target)
    return analytics.linear_search(cleaned, target)
