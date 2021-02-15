def stock_availability(inventory_list, command, *args):
    if command == "delivery":
        inventory_list.extend(args)
    elif command == "sell":
        if args:
            data = [el for el in args]
            if type(data[0]) == int:
                num = int(data[0])
                inventory_list = inventory_list[num:]
            else:
                for el in data:
                    while el in inventory_list:
                        inventory_list.remove(el)
        else:
            inventory_list = inventory_list[1:]
    return inventory_list




















print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
