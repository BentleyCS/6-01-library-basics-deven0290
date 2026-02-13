import analytics


def _try_call(names, *args):
    """Try calling the first analytics function that exists in `names`."""
    for name in names:
        fn = getattr(analytics, name, None)
        if callable(fn):
            return fn(*args)
    return None


def _pretty_number(x):
    """Return int if it's basically a whole number, otherwise a rounded float."""
    if abs(x - round(x)) < 1e-9:
        return int(round(x))
    return round(x, 2)


def process_expenses(rawPrices):
    out = []
    for p in rawPrices:
        v = _try_call(
            ["add_percent", "addPercent", "increase_by_percent", "increaseByPercent"],
            p, 15
        )
        if v is None:
            v = p * 1.15
        out.append(_pretty_number(v))
    return out


def analyze_scores(n):
    scores = []
    for i in range(n):
        scores.append(float(input(f"Enter score #{i + 1}: ")))

    high = _try_call(["find_max", "findMax", "get_max", "getMax", "maximum"], scores)
    if high is None:
        high = max(scores)

    avg = _try_call(["average", "avg", "mean", "get_average", "getAverage"], scores)
    if avg is None:
        avg = sum(scores) / len(scores) if scores else 0

    return _pretty_number(high), _pretty_number(avg)


def sanitize_usernames(usernames):
    cleaned = []
    for s in usernames:
        no_spaces = _try_call(
            ["remove_spaces", "removeSpaces", "strip_spaces", "stripSpaces"],
            s
        )
        if no_spaces is None:
            no_spaces = "".join(s.split())  # removes ALL whitespace

        lower = _try_call(
            ["to_lower", "toLower", "lower_case", "lowerCase"],
            no_spaces
        )
        if lower is None:
            lower = no_spaces.lower()

        cleaned.append(lower)
    return cleaned


def identify_outliers(values):
    filtered = _try_call(["filter_over", "filterOver", "above", "above_value"], values, 100)
    if filtered is not None:
        return filtered
    return [v for v in values if v > 100]


def search_and_report(items):
    cleaned = sanitize_usernames(items)
    target = "".join(input("Item to search for: ").split()).lower()

    is_sorted = _try_call(["is_sorted", "isSorted", "sorted_check", "sortedCheck"], cleaned)
    if is_sorted is None:
        is_sorted = all(cleaned[i] <= cleaned[i + 1] for i in range(len(cleaned) - 1))

    if is_sorted:
        idx = _try_call(["binary_search", "binarySearch"], cleaned, target)
        if idx is not None:
            return idx

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

    idx = _try_call(["linear_search", "linearSearch"], cleaned, target)
    if idx is not None:
        return idx

    for i, x in enumerate(cleaned):
        if x == target:
            return i
    return -1
