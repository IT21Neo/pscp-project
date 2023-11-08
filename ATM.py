"""อยากลาออก"""
def main():
    '''ลาออกดีกว่า'''
    money = int(input())
    bank_acc = 0
    bank_acc += money
    while True:
        order = input()
        if order == 'END':
            break
        order = list(order.split(" "))
        if order[0] == 'D':
            bank_acc += int(order[1])
        elif order[0] == 'W':
            if int(order[1]) > bank_acc:
                bank_acc = 0
            else:
                bank_acc -= int(order[1])
    print(bank_acc)
main()
