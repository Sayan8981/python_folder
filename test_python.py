## to get find out maximum profit from price_list with price_list first_index = buy and second index = sell respectively.

price_list = [500,120,130,250,100,80]
profit_dict = dict()

for price_index in range(0,len(price_list)):
    buy_price = price_list[price_index]
    while price_index < len(price_list) - 1:
        price_index += 1
        sell_price = price_list[price_index]
        temp_profit = sell_price - buy_price
        if (sell_price - buy_price) > 0 or (sell_price - buy_price) > temp_profit:
            profit_dict.update ({"%s"%price_index: sell_price - buy_price})

print ({str(max(profit_dict,key = lambda x: profit_dict[x])): profit_dict.get(max(profit_dict,key = lambda x: profit_dict[x]))})            