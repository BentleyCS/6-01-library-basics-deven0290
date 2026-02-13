from decimal import Decimal, ROUND_HALF_UP

def add_percent(value, percent):
    
    v = Decimal(str(value))
    p = Decimal(str(percent))
    out = (v * (Decimal("100") + p) / Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


    if out == out.to_integral_value():
        return int(out)
    return float(out)

def average(nums):
    if not nums:
        return 0
    out = sum(nums) / len(nums)
   
    if abs(out - round(out)) < 1e-9:
        return int(round(out))
    return out

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
