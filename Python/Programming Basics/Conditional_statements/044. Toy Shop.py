tripPrice = float(input())
puzzleCount = int(input())
dollCount = int(input())
bearCount = int(input())
minionCount = int(input())
truckCount = int(input())

totalCount = puzzleCount + dollCount + bearCount + minionCount + truckCount


totalMoney = (puzzleCount*2.60) + (dollCount*3) + (bearCount*4.10) + (minionCount*8.20) + (truckCount*2)

if totalCount >= 50:
    discount = totalMoney*0.25
    totalMoney -= discount

rent = totalMoney*0.1
totalMoney = totalMoney - rent

if totalMoney >= tripPrice:
    print(f"Yes! {totalMoney-tripPrice:0.2f} lv left.")
else:
    print(f"Not enough money! {tripPrice-totalMoney:.2f} lv needed.")