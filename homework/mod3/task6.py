ints = [int(x) for x in input().split()]
verdict = len(ints) != len(set(ints))
print(verdict)
