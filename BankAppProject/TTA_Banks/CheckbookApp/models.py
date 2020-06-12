from django.db import models

# Create your models here.

# Choices
TRANSACTION_TYPE = [
    ('withdrawal', 'Withdrawal'),
    ('deposit', 'Deposit'),
]

class UserAccount(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    starting_balance = models.DecimalField(max_digits=15, decimal_places=2)

    UserAccounts = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserTransaction(models.Model):
    transaction_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    transaction_type = models.CharField(max_length=120, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(max_length=1000)
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    UserTransactions = models.Manager()

    def __str__(self):
        return str(self.account)