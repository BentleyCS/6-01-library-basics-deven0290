from decimal import Decimal, ROUND_HALF_UP

def _to_decimal(x):
    return Decimal(str(x))

def nice_number(x):
    """Convert Decimals/floats to int if whole, else float."""
    if isinstance(x, Decimal):
        if x == x.to_integral_value():
            return int(x)
        return float(x)
    # float/int
    if isinstance(x, (int,)):
        return x
    if isinstance(x, float) and abs(x - round(x)) < 1e-9:
        return int(round(x))
    return x

def add_percent(value, percent):
    v = _to_decimal(value)
    p = _to_decimal(percent)
    out = (v * (Decimal("100") + p) / Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return nice_number(out)

def average(nums):
    if not nums:
        return 0
    total = sum(nums)
    avg = total / len(nums)
    
    return nice_number(float(avg))

def find_max(nums):
    return max(nums) if nums else None

def remove_spaces(s):
    return "".join(str(s).split())

def to_lower(s):
    return str(s).lower()

def filter_over(values, threshold):
    return [v for v in values if v > threshold]

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def linear_search(lst, target):
    for i, x in enumerate(lst):
        if x == target:
            return i
    return -1

def binary_search(lst, target):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
