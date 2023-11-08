"""OTP"""
def main():
    """Demo"""
    while True:
        num = input()
        if num == "0":
            break
        otp = [num.count(str(i)) for i in range(10)]
        if len(num) == 4 and otp.count(2) == 1:
            print("Valid")
        elif len(num) == 6 and (otp.count(2) == 2 or otp.count(3) == 1):
            print("Valid")
        elif len(num) == 8 and (otp.count(3) == 2 or otp.count(2) == 3):
            print("Valid")
        else:
            print("Invalid")
main()
