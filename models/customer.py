class Customer:
    def __init__(self , customer_id , name, email, phone ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def return_details(self):
        return f"{self.customer_id} {self.name} {self.email} {self.phone}"