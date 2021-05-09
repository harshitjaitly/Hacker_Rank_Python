# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
bill = OrderedDict()
for _ in range(int(input())):
    item_name , price = input().rsplit(" ", 1)
    # try :
    #     bill[item_name] += int(price)
    # except :
    #     bill[item_name] = int(price)
    bill[item_name] = bill.get(item_name,0)+int(price)

for item,price in bill.items():
    print(item, price)
