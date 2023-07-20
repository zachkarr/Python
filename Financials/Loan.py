# Loan class - calculates loans


class Loan:
    """Loan Calculator"""

    def __init__(self, amount=0.0, rate=0.0, term=0):
        self.set_amount(amount)
        self.set_rate(rate)
        self.set_term(term)
        self.validate()
        if self._isvalid:
            self.build_loan()

    def set_amount(self, amount):
        # internal variables using self are pseudo private
        self._amount = amount

    def get_amount(self):
        return self._amount

    def set_rate(self, rate):
        self._rate = rate

    def get_rate(self):
        return self._rate

    def set_term(self, term):
        self._term = term

    def get_term(self):
        return self._term

    def validate(self):
        self._error = ""
        self._isvalid = True
        if self._amount <= 0:
            self._error = "Loan amount must be greater than 0 \n"
            self._isvalid = False
        if self._rate < 1 or self._rate > 25:
            self._error += (
                " Rate appears to be out of bounds (must be between 1 and 25) \n"
            )
            self._isvalid = False
        if self._term <= 0:
            self._error += "Term must be greater than 0 \n"
            self._isvalid = False

    def is_valid(self):
        return self._isvalid

    def get_error_message(self):
        return self._error

    def build_loan(self):
        self._beginning_balance = [0] * self._term
        self._interest_charged = [0] * self._term
        self._ending_balance = [0] * self._term
        monthly_rate = self._rate / 12.0 / 100
        self._monthly_payment = (
            self._amount
            * (monthly_rate * (1 + monthly_rate) ** self._term)
            / ((1 + monthly_rate) ** self._term - 1)
        )
        self._interest_charged[0] = self._amount * monthly_rate
        self._beginning_balance[0] = self._amount
        self._ending_balance[0] = self._amount + self._interest_charged[0] - self._monthly_payment
        for i in range(0, self._term):
            if i > 0:
                self._beginning_balance[i] = self._ending_balance[i -1]
                self._interest_charged[i] = self._beginning_balance[i] * monthly_rate
                self._ending_balance[i] = (
                    self._beginning_balance[i] + self._interest_charged[i] - self._monthly_payment
                )

    def get_monthly_payment(self):
        return self._monthly_payment

    def get_interest(self):
        total_interest = self._interest_charged[0]
        for i in range(0, self._term):
            if i > 0:
                total_interest += self._interest_charged[i]
        return total_interest

    def get_beginning_balance(self, month):
        if month < 1 or month > self._term:
            return -1
        return self._beginning_balance[month - 1]

    def get_interest_charged(self, month):
        if month < 1 or month > self._term:
            return -1
        return self._interest_charged[month - 1]

    def get_ending_balance(self, month):
        if month < 1 or month > self._term:
            return -1
        return self._ending_balance[month - 1]
