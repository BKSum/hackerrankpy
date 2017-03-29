if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arrSet = sorted(set(arr))
    print arrSet[-2] if len(arrSet)>1 else arrSet[0]
