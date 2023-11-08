"""Music Lover"""
def main():
    """Demo"""
    line = int(input())
    song_dict = {}
    for _ in range(line):
        song = input().strip().split("-")
        if song[0] not in song_dict:
            song_dict[song[0]] = [song[1]]
        else:
            song_dict[song[0]].append(song[1])
    for i in song_dict:
        print(i)
        print(*song_dict[i], sep='\n')
main()
