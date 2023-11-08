"""ScaledMatrix"""
def main(rows, cols):
    """Demo"""
    tmp = ""
    lsttmp = list(tmp)
    ans = []
    count = 0
    lsttmp = [float(input()) for _ in range(rows*cols)]
    for i in lsttmp:
        nowpercent = round((i - min(lsttmp)) / (max(lsttmp) - min(lsttmp)), 2)
        ans.append(nowpercent)
    for _ in range(rows):
        for _ in range(cols):
            tmp += ("%.2f"% (ans[count])) + " "
            count += 1
        print(tmp)
        tmp = ""
main(int(input()), int(input()))

