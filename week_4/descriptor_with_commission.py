class Value:
    def __init__(self):
        self.amount = None
    def __get__(self, obj, obj_type):
        if not self.amount:
            return
        else:
            return self.amount - self.amount * obj.commission
    def __set__(self, obj, value):
        self.amount = value

class Account:
    amount = Value()
    def __init__(self, commission):
        self.commission = commission

# a = Account(0.5)
# print(a.amount)
# a.amount = 200
# print(a.amount)

