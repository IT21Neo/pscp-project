"""Coupon"""
def main():
    """https://www.youtube.com/watch?v=794QQ96ZrjA"""
    price = float(input())
    discount_1 = (input()).split()
    discount_2 = (input()).split()
    dis_ab = price - float(discount_1[0]) if price >= float(discount_1[1]) else price
    dis_xy = price*((100 - float(discount_2[0]))/100) if price >= float(discount_2[1]) else price
    if dis_ab < dis_xy:
        print("1 %.1f"% dis_ab)
    elif dis_ab > dis_xy:
        print("2 %.1f"% dis_xy)
    elif dis_ab == price and dis_xy == price:
        print("Nope")
    elif dis_ab == dis_xy:
        if discount_1[1] <= discount_2[1]:
            print("1 %.1f"% dis_ab)
        else:
            print("2 %.1f"% dis_xy)
main()
