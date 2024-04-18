inventory_data = [
    {"product": "Milk", "sold": 25, "store": "East"},
    {"product": "Eggs", "sold": 50, "store": "North"},
    {"product": "Bread", "sold": 20, "store": "East"},
    {"product": "Milk", "sold": 15, "store": "West"},
    {"product": "Eggs", "sold": 30, "store": "East"},
    {"product": "Milk", "sold": 10, "store": "North"}
]

newlist={}
for i in inventory_data:
    product=i["product"]
    sold=i["sold"]
    store=i["store"]
    #print(product,sold,store)

    if product not in newlist:
        newlist[product]={"amount_sold":0,"store":[]}
        print(newlist)
    newlist[product]["amount_sold"]=newlist[product]["amount_sold"]+sold

    if store not in newlist[product]["store"]:
        newlist[product]["store"].append(store)
        

for key,value in newlist.items():
    print(key,value)


"""
what i learned here is that i can acess subkeys in dictionary by doing dictionaryname[firstkey][subkey]
"""
