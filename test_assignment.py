import builtins
import main

def test_smoke():
    assert True

def test_process_expenses():
    out = main.process_expenses([100, 0])
    assert out[0] == 115
    assert out[1] == 0

def test_analyze_scores(monkeypatch):
    fake_inputs = iter(["10", "20", "30"])
    monkeypatch.setattr(builtins, "input", lambda _: next(fake_inputs))

    high, avg = main.analyze_scores(3)
    assert high == 30
    assert avg == 20

def test_sanitize_usernames():
    assert main.sanitize_usernames(["  Apple", "Banana ", "  CHERRY  "]) == [
        "apple", "banana", "cherry"
    ]

def test_identify_outliers():
    assert main.identify_outliers([50, 101, 100, 250]) == [101, 250]

def test_search_and_report_sorted(monkeypatch):
    items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
    monkeypatch.setattr(builtins, "input", lambda _: "cherry")
    assert main.search_and_report(items) == 2

def test_search_and_report_unsorted(monkeypatch):
    items = ["zebra", "  Apple", "mango"]
    monkeypatch.setattr(builtins, "input", lambda _: "apple")
    assert main.search_and_report(items) == 1
