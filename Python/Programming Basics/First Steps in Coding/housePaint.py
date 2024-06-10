x = float(input())
y = float(input())
h = float(input())

frontWall = (x * x - (2*1.2)) * 2 + (2*1.2)
sideWall = (x * y - (1.5 * 1.5)) * 2

topQuad = x * y * 2
topTria = (x*h/2) * 2

greenPaint = (frontWall+sideWall) / 3.4
redPaint = (topQuad+topTria) / 4.3

print(f"{greenPaint:.2f}")
print(f"{redPaint:.2f}")