"""Inverter"""
def main(bina):
    """Demo"""
    tmp = ""
    for i in bina:
        if i == "0":
            tmp += "1"
        elif i == "1":
            tmp += "0"
    for i in range(len(tmp)):
        if tmp[i] == "1":
            print(tmp[i:])
            break
main(input())
