"""Poisonous Vegetables"""
import json
def check_vegan(plant, size):
    """https://www.youtube.com/watch?v=T8y_RsF4TSw"""
    out = ""
    if plant[1] > size:
        out = '[ - ]'
    else:
        if plant[2] - plant[0] == 0:
            out = '[ o ]'
        else:
            out = '[ x ]'
    return out

def main():
    """Demo"""
    plots = input().split(" x ")
    size = int(input())
    _ = int(input())
    farm = []
    for _ in range(int(plots[0])):
        vegans = input().replace(' ', ',')
        vegans = "[" + vegans.replace('][', '], [') + "]"
        vegans = json.loads(vegans)
        farm.append(vegans)
    for i in farm:
        current = ""
        for j in i:
            current += check_vegan(j, size)
        print(current)
main()
