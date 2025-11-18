# Simple Train Ticket Booking Program

def book_ticket():
    print("=== Welcome to Indian Railways ===")
    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    from_place = input("Enter starting station: ")
    to_place = input("Enter destination station: ")

    print("\nSelect Train Class:")
    print("1. Sleeper (₹500)")
    print("2. AC (₹1000)")
    print("3. First Class (₹1500)")

    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        cost = 500
        tclass = "Sleeper"
    elif choice == 2:
        cost = 1000
        tclass = "AC"
    elif choice == 3:
        cost = 1500
        tclass = "First Class"
    else:
        print("Invalid choice! Booking cancelled.")
        return
    qty = int(input("Enter number of tickets: "))
    total_fare = lambda c, q: c * q
    total = total_fare(cost, qty)
    if age >= 60:
        discount = 0.2 * total  
        total -= discount
        print("\nSenior citizen discount applied (20%)")

    print("\n===== Ticket Details =====")
    print("Passenger Name:", name)
    print("Age:", age)
    print("From:", from_place)
    print("To:", to_place)
    print("Class:", tclass)
    print("Tickets:", qty)
    print("Total Fare: ₹", total)
    print("===========================")
book_ticket()