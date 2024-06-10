poolSize = int(input())
firstPipePH = int(input())
secondPipePH = int(input())
missingHours = float(input())

firstPipePH *= missingHours
secondPipePH *= missingHours

waterInPool = firstPipePH + secondPipePH

if waterInPool <= poolSize:
    print(f"The pool is {waterInPool/poolSize*100:.2f}% full. Pipe 1: {firstPipePH/waterInPool*100:.2f}%. Pipe 2: {secondPipePH/waterInPool*100:.2f}%.")
else:
    print(f"For {missingHours} hours the pool overflows with {waterInPool-poolSize:.2f} liters.")
