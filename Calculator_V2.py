"""Calculator V2"""
def main(num=int):
    """Demo"""
    if num == 1:
        print(1)
    else:
        print(sum([((min(10**i-1, num)) - 10**(i-1) + 1)*i for i in range(1, len(str(num))+1)])+num)
main(int(input()))
