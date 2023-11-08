"""Rungame"""
def main(num):
    """https://www.youtube.com/watch?v=h-KuoHHjGRs"""
    run = [abs(0 - num[i]) if i == 0 else abs(num[i] - num[i-1]) for i in range(len(num))]
    print(sum(run))
main(tuple(map(int, input().split())))
