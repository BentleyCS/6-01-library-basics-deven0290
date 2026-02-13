import analytics
def process_expenses(rawPrices):
def analyze_scores(n):
def sanitize_usernames(usernames):
def identify_outliers(values):
def search_and_report(items):

import analytics

def process_expenses(rawPrices):
    return [p * 1.15 for p in rawPrices] 

def analyze_scores(n):
    scores = []
    for _ in range(n):
        scores.append(float(input("")))
    return max(scores), sum(scores) / len(scores)

def sanitize_usernames(usernames):
    return ["".join(s.split()).lower() for s in usernames]

def identify_outliers(values):
    return [v for v in values if v > 100]

def search_and_report(items):
    cleaned = sanitize_usernames(items)
    target = "".join(input("").split()).lower()

    sorted_ok = True
    for i in range(len(cleaned) - 1):
        if cleaned[i] > cleaned[i + 1]:
            sorted_ok = False
            break

    if sorted_ok:
        lo, hi = 0, len(cleaned) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if cleaned[mid] == target:
                return mid
            if cleaned[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    for i, x in enumerate(cleaned):
        if x == target:
            return i
    return -1
