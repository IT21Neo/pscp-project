"""Difference"""
import json
def main():
    """https://www.youtube.com/watch?v=N9bashij_7c"""
    word_lst1 = json.loads(input())
    word_lst2 = json.loads(input())
    word_set = set(word_lst1 + word_lst2)
    ans = []
    for i in word_set:
        if word_lst1.count(i) - word_lst2.count(i) != 0:
            ans.append([i, abs(word_lst1.count(i) - word_lst2.count(i))])
    if ans:
        for i in sorted(ans):
            print(*i)
    else:
        print("ONAJI DAYO!")
main()
