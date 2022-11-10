s = ""

def season(month):
    global s
    if month == 12 or 1 <= month <= 2:
        s = "Зима"
    elif 3 <= month <= 5:
        s = "Весна"
    elif 6 <= month <= 8:
        s = "Лето"
    elif 9 <= month <= 11:
        s = "Осень"
    return s