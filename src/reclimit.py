import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)
print(sys.getrecursionlimit())