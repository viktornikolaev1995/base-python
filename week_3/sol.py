import os, csv
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        if os.path.splitext(self.photo_file_name)[1] in [".jpg", ".jpeg", ".png", ".gif"]:
            return os.path.splitext(self.photo_file_name)[1]
        raise Exception("Недопустимое расширение файла изображения!")


class Car(CarBase):
    car_type = "car"
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = "truck"
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if self.body_whl and isinstance(self.body_whl, str):
            try:
                self.body_length, self.body_width, self.body_height = (float(i) for i in self.body_whl.split("x"))
            except ValueError:
                print(f"Введено невалидное значение body_whl: {body_whl} для объекта {self.__class__}")
                self.body_length = self.body_width = self.body_height = 0.0
        else:
            self.body_length = self.body_width = self.body_height = 0.0
    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height



class SpecMachine(CarBase):
    car_type = "spec_machine"
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def check_brand(j, type):
    if j and isinstance(j, str) and j[0].isupper() and j[0].isalpha() and not (j.replace(".", "0").isdigit() or j.isdigit()) \
            and j != type:
        brand = j
        return brand
def check_photo_file_name(j):
    if j and isinstance(j, str) and (".jpeg" in j or ".png" in j or ".gif" in j or ".jpg" in j) and len(j.split(".")) == 2 \
            and j.split(".")[0] and j.split(".")[1] in ["jpeg", "jpg", "png", "gif"]:
        photo_file_name = j
        return photo_file_name

def check_carrying(j, type):

    if j and (j.replace(".", "0").isdigit() or j.isdigit()) and j != type:
        carrying = j
        return carrying



def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        next(reader)
        car_list = []
        for row in reader:
            if "car" in row:
                a_ = {}
                for j in row:
                    if check_brand(j,"car"):
                        a_.update({'brand': check_brand(j, "car")})
                    elif check_photo_file_name(j):
                        a_.update({'photo_file_name': check_photo_file_name(j)})

                    elif j and j.replace(".", "0").isdigit() and "." in j and j != "car":
                        carrying = j
                        a_.update({'carrying': carrying})
                    elif j and j.replace(".", "0").isdigit() and "." not in j and j != "car":
                        passenger_seats_count = j
                        a_.update({'passenger_seats_count': passenger_seats_count})


                if 'brand' in a_.keys() and "photo_file_name" in a_.keys() and "carrying" in a_.keys() \
                        and 'passenger_seats_count' in a_.keys():
                    car = Car(a_['brand'], a_['photo_file_name'], a_['carrying'], a_['passenger_seats_count'])
                    car_list.append(car)


            elif "truck" in row:
                a_ = {}
                for j in row:
                    if check_brand(j, "truck"):
                        a_.update({'brand': check_brand(j, "truck")})
                    elif check_photo_file_name(j):
                        a_.update({'photo_file_name': check_photo_file_name(j)})
                    elif check_carrying(j, "truck"):
                        a_.update({'carrying': check_carrying(j, "truck")})
                    elif j and j.count("x") > 1:
                        body_whl = j
                        a_.update({'body_whl': body_whl})
                if 'body_whl' not in a_.keys():
                    a_.update({'body_whl': ""})

                if 'brand' in a_.keys() and "photo_file_name" in a_.keys() and "carrying" in a_.keys():
                    truck = Truck(a_['brand'], a_['photo_file_name'], a_['carrying'], a_['body_whl'])
                    car_list.append(truck)

            elif row[0] == "spec_machine":
                a_ = {}
                if len(row) == 7:
                    if row[1] and not (row[1].replace(".", "0").isdigit() or row[1].isdigit()) and row[1] != "spec_machine":
                        a_.update({'brand': row[1]})

                    if row[3] and (".jpeg" in row[3] or ".png" in row[3] or ".gif" in row[3] or ".jpg" in row[3]) and \
                            len(row[3].split(".")) == 2 and row[3].split(".")[0] and row[3].split(".")[1] in ["jpeg", "jpg", "png", "gif"]:
                        a_.update({'photo_file_name': row[3]})


                    if row[5] and (row[5].replace(".", "0").isdigit() or row[5].isdigit()):
                        a_.update({'carrying': row[5]})

                    if row[6]:
                        a_.update({'extra': row[6]})

                if 'brand' in a_.keys() and 'photo_file_name' in a_.keys() and "carrying" in a_.keys() \
                        and "extra" in a_.keys():
                    spec_machine = SpecMachine(a_['brand'], a_['photo_file_name'], a_['carrying'], a_['extra'])
                    car_list.append(spec_machine)

        return car_list