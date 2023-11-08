"""Coke"""
def cokepro():
    """Demo"""
    price = int(input())
    laek = int(input())
    newprice = int(input())
    want = int(input())
    money = 0
    if laek == 0:
        money += want*price
    elif newprice <= price:
        promotion = want//laek
        money += promotion*newprice
        if want % laek == 0 and want//laek != 0:
            promotion -= 1
            money -= newprice
        money += (want-promotion)*price
    print(money)
cokepro()
