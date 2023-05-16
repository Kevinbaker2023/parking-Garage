# Start Your Code here
class ParkingGarage():
    def __init__(self, available_tickets = [100], available_parking_spaces = [100]):
        self.available_tickets = available_tickets
        self.available_parking_spaces = available_parking_spaces

    def is_Available(self):
        if self.available_tickets[0] > 0 and self.available_parking_spaces[0] > 0:
            return True
        else:
            return False
        
    def issue_tickets(self):
        if self.is_Available() == True:
            self.available_tickets[0] -= 1
            self.available_parking_spaces[0] -= 1
            print(f'Tickets available: {self.available_tickets}')
            print(f'Parking spaces available: {self.available_parking_spaces}')
            print("Ticket issued. Please proceed to park")
        else:
            print("Sorry, the ParkingGarage is currently full, please try again later.")
        
    def pay_For_Parking(self):
        self.currentTicket = {
            'Paid': 'False'
        }
        paid = float(input('Please enter your payment amount: '))
        if paid > 0:
            self.currentTicket['Paid'] = 'True'
            print('Your ticket has been paid, you now have 15 minutes to leave.')

    def leave_Garage(self):
        for value in self.currentTicket.values():
            if value == 'True':
                print('Thank you, have a nice day')
            elif value == 'False':
                paid1 = float(input('Please enter your payment amount here!: '))
                if paid1 > 0:
                    print("Thank you, have a nice day!")
                else:
                    print(float(input('Please enter the correct amount: ')))
        self.available_tickets = [i + 1 for i in self.available_tickets]
        print(f'Tickets available: {self.available_tickets}')
        self.available_parking_spaces = [j + 1 for j in self.available_parking_spaces]
        print(f'Parking spaces available: {self.available_parking_spaces}')

    def runner(self):
        print('Enter quit to exit')
        while True:
            response = input('Would you like to enter, pay, or leave: ').lower()
        
        
            if response == 'quit':
                break
            elif response == 'enter':
                self.is_Available()
                self.issue_tickets()
            elif response == 'pay':
                self.pay_For_Parking()
            elif response == 'leave':
                self.leave_Garage()
            else:
                print('Response not recognized, please try again')

# new_ticket = ParkingGarage()
# print(new_ticket.is_Available())
# print(new_ticket.issue_tickets())
# print(new_ticket.pay_For_Parking())
# print(new_ticket.leave_Garage())

new_ticket = ParkingGarage()
new_ticket.runner()