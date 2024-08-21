class Bus:

    def __init__(self, max_seats: int, max_speed: int, passengers: list):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = passengers
        self.available = True
        self.seats = {
            seat: passengers[seat] if seat < len(passengers) else None
            for seat in range(max_seats)
        }

    def __contains__(self, passenger):
        try:
            self.passengers.index(passenger)
            return True
        except ValueError as e:
            return False

    def __add__(self, passenger):
        self.__check_available
        if self.available:
            for seat, taken in self.seats.items():
                if not taken:
                    self.seats[seat] = passenger
                    self.passengers.append(passenger)
                    break
        else:
            print("There are no available seats")

    def __sub__(self, passenger):
        try:
            index = self.passengers.index(passenger)
            self.passengers.pop(index)
            for seat, taken in self.seats.items():
                if taken == passenger:
                    self.seats[seat] = None
                    break
            print(f"{passenger} got out of the bus")
        except ValueError as e:
            print(f"{passenger} was not found")

    def __check_available(self):
        total_available = list(self.seats.values()).count(None)
        if total_available == 0:
            self.available = False
        else:
            self.available = True

    def out_bus(self, amount: int):
        if self.passengers:
            for seat in range(amount):
                self.seats[seat] = None
                self.passengers.pop(seat)
        else:
            print("There are no passengers")

    def in_bus(self, passengers: list):
        for passenger in range(len(passengers)):
            self.__check_available()
            if self.available:
                for seat, taken in self.seats.items():
                    if not taken:
                        self.seats[seat] = passengers[passenger]
                        self.passengers.append(passengers[passenger])
                        break
            else:
                print(f"There are no availble seats for {passengers[passenger:]}")
                break

    def increase_speed(self, amount):
        self.speed = (
            self.max_speed
            if self.speed + amount > self.max_speed
            else self.speed + amount
        )

    def decrease_speed(self, amount):
        self.speed = 0 if self.speed - amount < 0 else self.speed - amount


gaz = Bus(10, 100, ["Yabusido", "Petrov", "Kiroma", "Levito", "Pancheto"])
gaz.increase_speed(50)
gaz.decrease_speed(28)
print(gaz.speed)
gaz - "Kiroma"
gaz + "Petrova"
print(gaz.seats)
print(gaz.passengers)
