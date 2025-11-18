trains = {
    101: {"name": "Express", "seats": 50, "fare": 150.00},
    102: {"name": "Superfast", "seats": 25, "fare": 250.00},
}

# A list to store booked tickets
bookings = []
pnr_counter = 1000 # Start PNR numbers from 1000

def show_trains():
    """Display available trains and their details."""
    print("Available Trains:")
    print("---------------------------------------")
    print("Train No. | Name      | Available Seats | Fare")
    print("---------------------------------------")
    for train_no, details in trains.items():
        print(f"{train_no:<10}| {details['name']:<10}| {details['seats']:<16}| ${details['fare']:.2f}")
    print("---------------------------------------")

def book_ticket():
    """Handle the ticket booking process."""
    global pnr_counter
    try:
        train_no = int(input("Enter the train number you wish to book: "))
        if train_no not in trains:
            print("Invalid train number.")
            return
        
        train_details = trains[train_no]
        num_tickets = int(input(f"How many tickets would you like to book for the {train_details['name']}? "))
        
        if num_tickets > train_details['seats']:
            print("Sorry, not enough seats available.")
            return

        passenger_name = input("Enter your name: ")
        
        total_fare = num_tickets * train_details['fare']
        
        # Update available seats
        train_details['seats'] -= num_tickets
        
        # Generate PNR and save booking
        pnr_counter += 1
        pnr = pnr_counter
        booking_info = {
            "pnr": pnr,
            "train_no": train_no,
            "passenger_name": passenger_name,
            "tickets": num_tickets,
            "total_fare": total_fare
        }
        bookings.append(booking_info)
        
        print("\n--- Booking Confirmed! ---")
        print(f"PNR: {pnr}")
        print(f"Passenger: {passenger_name}")
        print(f"Train: {train_details['name']} ({train_no})")
        print(f"Tickets Booked: {num_tickets}")
        print(f"Total Fare: ${total_fare:.2f}")

    except ValueError:
        print("Invalid input. Please enter a number.")
        
def show_bookings():
    """Display all current bookings."""
    if not bookings:
        print("No bookings found.")
        return
        
    print("\n--- All Booked Tickets ---")
    for booking in bookings:
        print(f"PNR: {booking['pnr']} | Passenger: {booking['passenger_name']} | Train No: {booking['train_no']} | Tickets: {booking['tickets']}")
    print("----------------------------")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\n--- Welcome to the Train Ticket Booking System ---")
        print("1. Show available trains")
        print("2. Book a ticket")
        print("3. View all bookings")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            show_trains()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            show_bookings()
        elif choice == '4':
            print("Thank you for using our service. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu function when the script is executed
if __name__ == "__main__":
    main_menu()
