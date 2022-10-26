s = input().split()
lst = [int(c) for c in s]
lst.sort()
print(*lst)
lst.sort(reverse=True)
print(*lst)
