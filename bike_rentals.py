class Rentals:
    available = 15
    type_fare = {'Hourly':5,'Daily':20,'Weekly':60}
        
    def display_fare(self):
        print('Fare details: ')
        for i in Rentals.type_fare:
            print(f"per/{i}: {Rentals.type_fare[i]}$")
    def display_availability(self):
        print('Available number of bikes: ',Rentals.available)
    def request_bike(self):
        self.proceed = True
        while(self.proceed):
            self.req_num = int(input('Enter the number of bikes required: '))
            if(self.req_num > Rentals.available):
                print(f"Only {Rentals.available} bikes are available.")
                self.proceed = True
            else:
                self.proceed = False
        self.req_basis = input('Select type (Hourly/Daily/Weekly): ')
        self.req_duration = int(input('Enter duration: '))
        self.request_submitted = True
        return self.request_submitted
    def issue_bill(self):
        self.bill_amount = self.req_num*Rentals.type_fare[self.req_basis]*self.req_duration
        print(f"Your total bill amount will be: {self.bill_amount}$")
    
r = Rentals()
r.display_fare()
r.display_availability()
requested = r.request_bike()
if requested:
    r.issue_bill()