class Expense:
    def __init__(self, username, amount, category, date, description, expense_id=None):
        self.expense_id = expense_id
        self.username = username
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return (f"Expense(id={self.expense_id}, username={self.username}, amount={self.amount}, "
                f"category={self.category}, date={self.date}, description={self.description})")
