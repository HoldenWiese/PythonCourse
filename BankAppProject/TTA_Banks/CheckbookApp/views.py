from django.shortcuts import render, get_object_or_404, redirect

from .models import *

from .forms import *


def home_view(request, *args, **kwargs):
    my_form = AccessAccountForm()
    if request.method == 'POST':
        my_form = AccessAccountForm(request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data
            pk = data['account_choice'].pk
            all_transactions = UserTransaction.UserTransactions.filter(account=pk)
            balance = data['account_choice'].starting_balance
            each_total = []
            for transaction in all_transactions:
                if transaction.transaction_type == 'deposit':
                    balance = balance + transaction.amount
                    each_total.append(balance)
                else:
                    balance = balance - transaction.amount
                    each_total.append(balance)
            balances = zip(each_total, all_transactions)
            context = {
                'account_details': data['account_choice'],
                'transactions': all_transactions,
                'balance': balance,
                'balances': balances
            }
            return render(request, "BalanceSheet.html", context)
    context = {
        'form': my_form
    }
    return render(request, "index.html", context)


def add_transaction(request, *args, **kwargs):
    my_form = AddTransactionForm()
    if request.method == 'POST':
        my_form = AddTransactionForm(request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data
            my_form = my_form.save(commit= False)
            my_form.save()
            return redirect(home_view)
    context = {
        'form': my_form,
    }
    return render(request, "AddTransaction.html", context)


def create_new_account(request, *args, **kwargs):
    my_form = CreateNewAccountForm()
    if request.method == 'POST':
        my_form = CreateNewAccountForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect(home_view)
    context = {
        'form': my_form
    }
    return render(request, "CreateNewAccount.html", context)


def balance_sheet(request, *args, **kwargs):
    return render(request, "BalanceSheet.html")
