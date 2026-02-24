import CSP_6_01_Library_Basics as HW
def test_process_expenses():
    assert HW.process_expenses([100, 200, 300, 400, 500]) == [115, 230, 345, 460, 575]


def test_analyze_scores():
    assert HW.analyze_scores([10,20,30,40,100]) == (100,40)


def test_sanitize_usernames():
    assert HW.sanitize_usernames(["  Lebron  ", " James", "The ", " Goat"]) == ["lebron","james","the","goat"]


def test_identify_outliers():
    assert HW.identify_outliers([10, 20, 30, 50, 105, 150, 20]) == [105, 150]


def test_search_and_report():
    assert HW.search_and_report(["  BANANAS", " Blender ", "Dinosaur", "Watermelon "], "Watermelon") == (["bananas","blender","dinosaur","watermelon"], 3)
