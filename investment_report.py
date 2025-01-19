
invested = 0
current = 0

num = int(input("No of investments:"))
for _ in range(num):

    inv = float(input("Invested amount:"))
    curr = float(input("Current amount:"))
    profit_loss = curr - inv
    
    invested += inv
    current += curr

    print("\n\tinvested\tcurrent\t\tProfit/Loss")
    print(f"\t{inv}\t\t{curr}\t\t{profit_loss}")

    if profit_loss < 0:
        print("\n\t\t\t\t\tLOSS")
    elif profit_loss > 0:
        print("\n\t\t\t\t\t\tPROFIT")
    else:
        print("\n\t\t\t\t\t\tNO PROFIT OR LOSS")

    tt_profit_loss = current - invested
    print("\n")
    print(f"Total\t{invested}\t\t{current}\t\t{tt_profit_loss}")

    if tt_profit_loss < 0:
        print("\t\t\t\t\tLOSS")
    elif tt_profit_loss >0:
        print("\t\t\t\t\tPROFIT")
    else:
        print("\t\t\t\t\tNO PROFIT OR LOSS")
    
    
