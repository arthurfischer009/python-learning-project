Aktienkurs = 155
MA = 145
Risikotoleranz = 0.05

preisdifferenz = (Aktienkurs-MA)/MA

if Aktienkurs > MA:
    print("Price is above the moving average.-Buy signal")
    if preisdifferenz < Risikotoleranz:
        print("Price difference is within risk tolerance.")
    else:
        print("Price difference exceeds risk tolerance.")
        print("Action: HOLD")  # Hold position if risk tolerance is exceeded
elif Aktienkurs < MA:
    print("Sell signal")
else:
    print("Price is equal to the moving average.")
    print("Action: HOLD")
