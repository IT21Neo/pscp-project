"""Fever"""
def main():
    """Demo"""
    temp = float(input())
    if temp >= 36 and temp < 38:
        print("No Fever")
    elif temp >= 38 and temp < 39:
        print("Mild Fever")
    elif temp >= 39 and temp < 40:
        print("High Fever")
    elif temp >= 40:
        print("Very High Fever")
main()
