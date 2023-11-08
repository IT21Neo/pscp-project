"""iPad Air"""
def main(color, capa, connect, available=True):
    """Demo"""
    capaprice = {64: 19900, 256: 24900}
    connect_want = {"Wi-Fi": 0, "Wi-Fi + Cellular": 4500}
    available = color in ('Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue')\
    and capa in capaprice and connect in connect_want
    print(capaprice[capa] + connect_want[connect] if available else "Not Available")
main(input(), int(input()), input())
