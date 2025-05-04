#creating CustomerOrdere class
class CustomerOrder:
    def __init__(self,orderID,customerName,orderAmount):
        self.OrderID=orderID
        self.CustomerNAme = customerName
        self.OrderAmount= orderAmount
    # calculate the total oreder amount
    def calculation_total(self,orders):
        total=0
        for order in orders:
            total+=order.OrderAmount
        return total
    #function for print the  orderId,customername,OrderAmount
    def details(self):
        print("OrderID :",self.OrderID,"    Customer name :",self.CustomerNAme,"    OrderAmount :",self.OrderAmount)



p1=CustomerOrder(1,"Apan",250)
p1.details()
p2=CustomerOrder(2,"Amit",350)
p2.details()
p3=CustomerOrder(3,"Shihab",150)
p3.details()
p4=CustomerOrder(4,"Avishek",400)
p4.details()
p=[p1,p2,p3,p4]

TotalAmount=CustomerOrder.calculation_total(p)
print(TotalAmount)
