class User:
    def __init__(self, username, password, email=None, full_name=None, age=None, address=None, phone_number=None, pan_number=None, wallet_balance=0.0):
        self.username = username
        self.password = password
        self.email = email
        self.full_name = full_name
        self.age = age
        self.address = address
        self.wallet_balance = wallet_balance

    def __str__(self):
        return (f"User(username={self.username}, full_name={self.full_name}, email={self.email}, age={self.age}, "
                f"address={self.address}, phone_number={self.phone_number}, pan_number={self.pan_number}, "
                f"wallet_balance={self.wallet_balance})")
