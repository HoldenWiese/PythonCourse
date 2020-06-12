from django import forms
from django.forms import ModelForm

from .models import *


class AccessAccountForm(forms.Form):
    account_choice = forms.ModelChoiceField(queryset=UserAccount.UserAccounts.all())


class AddTransactionForm(ModelForm):
    class Meta:
        model = UserTransaction
        fields = '__all__'
        # fields = ['account', 'transaction_type', 'amount', 'description']

class CreateNewAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'
