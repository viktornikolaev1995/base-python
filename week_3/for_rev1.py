class Car:
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = passenger_seats_count

class Truck:
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = passenger_seats_count



a = [
["car", "Mazda", "4", "", "3.5", "mazda.jpeg"],
["truck", "Nissan", "4", "", "3.7", "nissan.jpeg"],
["car", "Toyota", "4", "", "3.9", "toyota.gif"],
["spec_machine", "Honda", "4", "", "3.1", "honda.png"],

]
b = []
for i in a:
    if "car" in i:
        a_ = {}
        for j in i:
            if j and isinstance(j, str) and not j.replace(".", "0").isdigit() and "." not in j and j != "car":
                brand = j
                a_.update({'brand': brand})
            elif j and isinstance(j, str) and not j.replace(".", "0").isdigit() and "." in j  and j != "car":
                photo_file_name = j
                a_.update({'photo_file_name': photo_file_name})
            elif j and j.replace(".", "0").isdigit() and "." in j  and j != "car":
                carrying = j
                a_.update({'carrying': carrying})
            elif j and j.replace(".", "0").isdigit() and "." not in j  and j != "car":
                passenger_seats_count = j
                a_.update({'passenger_seats_count': passenger_seats_count})
        print(a_)
        b1 = Car(a_['brand'], a_['photo_file_name'], a_['carrying'], a_['passenger_seats_count'])
        b.append(b1)
    elif "truck" in i:
        a1_ = {}
        for j in i:
            if j and isinstance(j, str) and not j.replace(".", "0").isdigit() and "." not in j and j != "car":
                brand = j
                a1_.update({'brand': brand})
            elif j and isinstance(j, str) and not j.replace(".", "0").isdigit() and "." in j and j != "car":
                photo_file_name = j
                a1_.update({'photo_file_name': photo_file_name})
            elif j and j.replace(".", "0").isdigit() and "." in j and j != "car":
                carrying = j
                a1_.update({'carrying': carrying})
            elif j and j.replace(".", "0").isdigit() and "." not in j and j != "car":
                passenger_seats_count = j
                a1_.update({'passenger_seats_count': passenger_seats_count})
        print(a1_)
        b1 = Truck(a1_['brand'], a1_['photo_file_name'], a1_['carrying'], a1_['passenger_seats_count'])
        b.append(b1)

print(b)
for car in b:
    print(type(car))