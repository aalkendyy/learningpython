class inventory:

    def __init__(self, item,qunatity):
        self.invdec={}
        self.item=item
        self.qunatity=qunatity
    def add(self,item,qunatity):
        if item in self.invdec:
            invdec[item]=invdec[item]+qunatity
        else:
            self.invdec[item]=qunatity

    def search(self,item):
        #self.item=item
        if item in self.invdec:
            print(f"Item: {item}, Quantity: {self.invdec[item]}")
        else:
            print(f"Item '{item}' not found in inventory.")

    def viewall(self):
        for i,y in self.invdec.items():
            print(i,y)
    def update(self,item,quantity):
        self.invdec[item]=self.invdec[item]+quantity

    def remove(self,item):
        del self.invdec[item]



my_inventory = inventory("chips", 5)
my_inventory2 = inventory("hotchips", 9)


my_inventory.add("chips", 7)
my_inventory2.add("hotchips", 9)
my_inventory2.add("hotchipslol", 9)
my_inventory.search("chips")
my_inventory2.remove("hotchipslol")
my_inventory2.search("hotchips")
my_inventory2.update("hotchips",20)
my_inventory2.viewall()


