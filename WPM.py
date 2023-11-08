"""WPM"""
def main(category, wordspeed):
    """main"""
    cat_dict = {"Kids": ["Very Slow", "Slow", "Average", "Fast", "Very Fast"],\
               "Adults": ["Very Slow", "Slow/Beginner", "Intermediate/Average", "Fast/Advanced",\
                           "Very Fast", "Insane"]}
    if category == "Kids":
        wpm = 4 if wordspeed > 40 else 3 if 31 <= wordspeed <= 40 else\
        2 if 21 <= wordspeed <= 30 else \
        1 if 11 <= wordspeed <= 20 else 0
    else:
        wpm = 5 if wordspeed > 80 else 4 if 66 <= wordspeed <= 80 else\
        3 if 46 <= wordspeed <= 65 else 2 if 36 <= wordspeed <= 45 else\
        1 if 26 <= wordspeed <= 35 else 0
    print(cat_dict[category][wpm])
main(input(), int(input()))
