import math

side = float(input())

perimeter = side * 4
area = side * side
diagonal = side * math.sqrt(2)

print(f"{perimeter:.2f}, {area:.2f}, {diagonal:.2f}, {math.sqrt(2):.10f}")