"""Area"""
def main():
    """Demo"""
    line = int(input())
    total = 0
    keep = []
    for _ in range(line):
        block = input()
        keep.extend(block)
    for i in keep:
        if i != " ":
            total += 1
    print(total)
main()
