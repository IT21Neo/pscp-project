"""Dart"""
def main(dart, score):
    """Demo"""
    for _ in range(dart):
        pos = input().split()
        posx = int(pos[0])
        posy = int(pos[1])
        shoot = (posx**2 + posy**2)**0.5
        if shoot <= 2:
            score += 5
        elif shoot <= 4:
            score += 4
        elif shoot <= 6:
            score += 3
        elif shoot <= 8:
            score += 2
        elif shoot <= 10:
            score += 1
    print(score)
main(int(input()), 0)
