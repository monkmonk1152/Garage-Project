class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {"paid": False}
            print(f"Ticket {ticket} issued. Please proceed to the parking space.")

    def payForParking(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.currentTicket and not self.currentTicket[ticket]["paid"]:
            amount = float(input("Enter the payment amount: "))
            if amount > 0:
                self.currentTicket[ticket]["paid"] = True
                print("Payment successful. You have 15 minutes to leave the garage.")
            else:
                print("Invalid payment. Please try again.")
        else:
            print("Invalid ticket or ticket already paid.")

    def leaveGarage(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]["paid"]:
                self.parkingSpaces.append(ticket)
                self.tickets.append(ticket)
                del self.currentTicket[ticket]
                print("Thank you for using this parking garage. Have a Amazing day and please come back!")
            else:
                print("Payment pending. Please make the payment before leaving.")
        else:
            print("Invalid ticket number.")


garage = ParkingGarage(100, 50)
while True:
    print("1. Take a ticket")
    print("2. Pay for parking")
    print("3. Leave the garage")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        garage.takeTicket()
    elif choice == 2:
        garage.payForParking()
    elif choice == 3:
        garage.leaveGarage()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
