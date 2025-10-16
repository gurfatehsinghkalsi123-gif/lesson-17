billamnt = int(input("enter the bill amount: "))
payment = int(input("enter your payment amount: "))
if billamnt>payment:
    print("you have pending payment of", billamnt-payment)
else:
    print("you submited the full payment, THANK YOU 😊")