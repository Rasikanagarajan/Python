from abc import ABC, abstractmethod
from datetime import datetime

#  PASSENGER 
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Passenger: {self.name} ({self.age} yrs)")


#  TRAIN 
class Train:
    def __init__(self, train_no, name, from_place, to_place, total_seats, fare):
        self.train_no = train_no
        self.name = name
        self.from_place = from_place
        self.to_place = to_place
        self.__total_seats = total_seats
        self.__available_seats = total_seats
        self.fare = fare

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            return True
        return False

    def cancel_seat(self):
        if self.__available_seats < self.__total_seats:
            self.__available_seats += 1

    def show_route(self):
        print(f"[{self.train_no}] {self.name}: {self.from_place} ➝ {self.to_place}")
        print(f"Seats Available: {self.__available_seats}/{self.__total_seats} | Fare: ₹{self.fare}")


#  PAYMENT 
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class OnlinePayment(Payment):
    def __init__(self, passenger):
        self.passenger = passenger

    def pay(self, amount):
        print(f"\nProcessing ₹{amount} for {self.passenger.name} ...")
        print("Payment Successful!")


# booking (encaps)
class Booking:
    def __init__(self, passenger, train, qty):
        self.passenger = passenger
        self.train = train
        self.qty = qty
        self.__fare = train.fare
        self.__total = self.__fare * qty
        self.status = "CONFIRMED"
        self.booking_time = datetime.now()

    def apply_discount(self):
        if self.passenger.age >= 60:
            discount = 0.2 * self.__total
            self.__total -= discount
            print("Senior Discount Applied (20%)")

    def get_total(self):
        return self.__total

    def show_ticket_details(self):
        print("\n********** TICKET DETAILS **********")
        print(f"Status: {self.status}")
        self.passenger.show_details()
        print(f"Train: {self.train.name}")
        self.train.show_route()
        print(f"Tickets: {self.qty}")
        print(f"Total Fare: ₹{self.__total}")
        print(f"Booked At: {self.booking_time.strftime('%d-%m-%y %H:%M:%S')}")
        if self.status == "CANCELLED":
            print(f"Cancelled At: {self.cancel_time.strftime('%d-%m-%y %H:%M:%S')}")
        print("***********************************")

# ticket
class Ticket(Booking, OnlinePayment):
    ticket_id_counter = 1000

    def __init__(self, passenger, train, qty):
        Booking.__init__(self, passenger, train, qty)
        OnlinePayment.__init__(self, passenger)
        Ticket.ticket_id_counter += 1
        self.ticket_id = Ticket.ticket_id_counter

    def issue(self):
        if self.status == "CANCELLED":
            print("Cannot issue a cancelled ticket.")
            return

        self.apply_discount()
        total = self.get_total()
        self.pay(total)
        print(f"\nTicket ID: {self.ticket_id}")
        self.show_ticket_details()

    def delete(self):
        if self.status == "CANCELLED":
            print("\nTicket is already cancelled.")
            return

        self.status = "CANCELLED"
        self.cancel_time = datetime.now()
        self.train.cancel_seat()

        print("\nTicket cancelled successfully.")
        print(f"Cancelled At: {self.cancel_time.strftime('%d-%m-%y %H:%M:%S')}")


# menu
class BookingSystem:
    def __init__(self):
        self.trains = [
            Train(101, "Chennai Express", "Chennai", "Delhi", 5, 1500),
            Train(102, "Bangalore Mail", "Bangalore", "Mumbai", 4, 1200),
            Train(103, "Coimbatore Express", "Coimbatore", "Chennai", 6, 800),
        ]
        self.bookings = []

    def show_trains(self):
        print("\nAvailable Trains:")
        for t in self.trains:
            t.show_route()

    def find_train(self, train_no):
        for t in self.trains:
            if t.train_no == train_no:
                return t
        return None

    def book_ticket(self):
        name = input("\nEnter passenger name: ")
        age = int(input("Enter age: "))
        passenger = Passenger(name, age)

        self.show_trains()
        train_no = int(input("Enter Train Number: "))
        train = self.find_train(train_no)

        if not train:
            print("Train not found!")
            return

        qty = int(input("Enter number of tickets: "))

        if not train.book_seat():
            print("No seats available!")
            return

        ticket = Ticket(passenger, train, qty)
        ticket.issue()
        self.bookings.append(ticket)

    def cancel_ticket(self):
        tid = int(input("Enter Ticket ID to cancel: "))
        for t in self.bookings:
            if t.ticket_id == tid:
                t.delete()
                return
        print("Ticket not found")

    def show_my_bookings(self):
        name = input("Enter passenger name: ").strip()
        found = False

        for t in self.bookings:
            if t.passenger.name.lower() == name.lower():
                print(f"\nTicket ID: {t.ticket_id}")
                t.show_ticket_details()
                found = True

        if not found:
            print("No bookings found for this passenger.")



def main():
    system = BookingSystem()

    while True:
        print("\n===== RAILWAY TICKET SYSTEM =====")
        print("1. Show Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Show My Bookings")
        print("5. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            system.show_trains()
        elif ch == "2":
            system.book_ticket()
        elif ch == "3":
            system.cancel_ticket()
        elif ch == "4":
            system.show_my_bookings()
        elif ch == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice!")

main()
