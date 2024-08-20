class Bus:

    def __check_empty_seats(self):
        total_empty_seats = list(self.seats.values()).count(None)
        if total_empty_seats == 0:
            self.empty_seats = False
        else:
            self.empty_seats = True

    def out_bus(self, amount):
        for seat in range(1, amount + 1):
            self.seats[seat] = None

    def in_bus(self, passengers):
        count = 0
        for seat, empty in self.seats.items():
            self.__check_empty_seats()
            if self.empty_seats:
                if not empty and count < len(passengers):
                    self.seats[seat] = passengers[count]
                    count += 1
                    print(self.seats)
            else:
                print(f"There are no empty seats for {passengers[count:]}")


seats = {seat: None for seat in range(1, 6)}
gaz = Bus(40, 5, 100, ["Tito", "Purchitta", "Monseno", "Kegren"], seats)
print(gaz.seats)
gaz.in_bus(["Ponto", "Gertemo", "Setiko"])
