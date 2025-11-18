from abc import ABC, abstractmethod
from datetime import datetime

# ------------------- 1. Train Class -------------------
class Train:
    def __init__(self, train_no, name, source, destination, total_seats, fare):
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.__total_seats = total_seats      # encapsulated
        self.__available_seats = total_seats  # encapsulated
        self.fare = fare

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            return True
        return False

    def cancel_seat(self):
        if self.__available_seats < self.__total_seats:
            self.__available_seats += 1

    def show_details(self):
        print(f"[{self.train_no}] {self.name}: {self.source} {self.destination}")
        print(f"Seats Available: {self.__available_seats}/{self.__total_seats} | Fare: ₹{self.fare}")
        # print("-" * 40)

# ------------------- 2. User Class -------------------
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def show_details(self):
        print(f"User: {self.name} ({self.age}) | Email: {self.email}")

# ------------------- 3. Abstraction (Payment) -------------------
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# ------------------- 4. OnlinePayment Class -------------------
class OnlinePayment(Payment):
    def __init__(self, user):
        self.user = user

    def pay(self, amount):
        print(f"Processing payment of ₹{amount} for {self.user.name} ...")
        print("✅ Payment successful!\n")

# ------------------- 5. Booking Class (Encapsulation + Inheritance) -------------------
class Booking(Train, User):
    def __init__(self, user, train):
        self.user = user
        self.train = train
        self.__status = "PENDING"
        self.booking_time = datetime.now()

    def confirm_booking(self):
        if self.train.book_seat():
            self.__status = "CONFIRMED"
        else:
            self.__status = "WAITING LIST"

    def cancel_booking(self):
        self.train.cancel_seat()
        self.__status = "CANCELLED"

    def _show_status(self):
        print(f"Booking Status for {self.user.name}: {self.__status}")

# ------------------- 6. Ticket Class (Multiple Inheritance + Polymorphism) -------------------
class Ticket(Booking, OnlinePayment):
    ticket_id_counter = 1000

    def __init__(self, user, train):
        Booking.__init__(self, user, train)
        OnlinePayment.__init__(self, user)
        Ticket.ticket_id_counter += 1
        self.ticket_id = Ticket.ticket_id_counter

    def issue_ticket(self):
        self.confirm_booking()
        self.pay(self.train.fare)
        self._show_status()
        print(f"🎟 Ticket ID: {self.ticket_id}")
        print(f"Passenger: {self.user.name} | Train: {self.train.name}")
        print(f"Route: {self.train.source} ➡ {self.train.destination}")
        print(f"Fare: ₹{self.train.fare}")
        print(f"Booked At: {self.booking_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)

# ------------------- 7. Booking System (Main Controller) -------------------
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
            t.show_details()

    def find_train(self, train_no):
        for t in self.trains:
            if t.train_no == train_no:
                return t
        return None

    def book_ticket(self):
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age: ").strip())
        email = input("Enter your email: ").strip()
        user = User(name, age, email)
        self.show_trains()
        train_no = int(input("Enter Train Number to Book: ").strip())
        train = self.find_train(train_no)
        if not train:
            print("❌ Train not found!")
            return
        ticket = Ticket(user, train)
        ticket.issue_ticket()
        self.bookings.append(ticket)

    def cancel_ticket(self):
        tid = int(input("Enter Ticket ID to cancel: "))
        for t in self.bookings:
            if t.ticket_id == tid:
                t.cancel_booking()
                print(f"❌ Ticket {tid} cancelled successfully.")
                return
        print("Ticket not found.")

    def show_my_bookings(self):
        email = input("Enter your email: ").strip()
        found = False
        for t in self.bookings:
            if t.user.email.lower() == email.lower():
                t.issue_ticket()
                found = True
        if not found:
            print("No bookings found for this email.")

# ------------------- 8. Main Menu -------------------
def main():
    system = BookingSystem()
    while True:
        print("\n===== TRAIN BOOKING SYSTEM =====")
        print("1. Show Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Show My Bookings")
        print("5. Exit")
        ch = input("Enter your choice: ").strip()

        if ch == "1":
            system.show_trains()
        elif ch == "2":
            system.book_ticket()
        elif ch == "3":
            system.cancel_ticket()
        elif ch == "4":
            system.show_my_bookings()
        elif ch == "5":
            print("Thank you for using Train Booking System!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()