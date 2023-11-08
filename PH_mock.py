"""PH (MockExam)"""
def main():
    """Demo"""
    phnum = float(input())
    if phnum < 7 and phnum >= 0:
        print("acidic")
    elif phnum > 7 and phnum <= 14:
        print("akaline")
    elif phnum == 7:
        print("neutral")
    else:
        print("error")
main()
