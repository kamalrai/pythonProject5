#Price of a house is $1M, If buyer has good credit, they need to put 10% otherwise they need to put down 20%.Preint down
# payment
price=100000
print(f"the price of house is {price}")
has_good_credit=True
if has_good_credit:
    down=10/100*price
else:
    down=20/100*price
print(f"the down payment is{down}")
