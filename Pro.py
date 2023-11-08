"""Pro"""
def main():
    """Demo"""
    comex = int(input())
    paidy = int(input())
    price = int(input())
    customer = int(input())
    promotion = (customer//comex)*paidy
    pay = (promotion + (customer%comex))*price
    print(pay)
main()
