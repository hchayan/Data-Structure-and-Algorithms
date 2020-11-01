def bonAppetit(bill, k, b):
    tmp = (sum(bill) - bill[k])//2
    if b - tmp != 0:
        print(b-tmp)
    else:
        print("Bon Appetit")


bonAppetit([3, 10, 2, 9], 1, 12)