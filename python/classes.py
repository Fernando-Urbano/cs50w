class Flight():
    def __init__(self, capacity):
        self.capacity = 0
        self.passengers = []

    def add_passenger(self, name):
        self.passengers.append(name)

    def open_seats(self):
        return self.capacity - len(self.open_seats)


flight = Flight(3)

people = ["Adriana", "Fernando", "Bruno", "Brenda"]
for person in people:
    flight.add_passenger(person)