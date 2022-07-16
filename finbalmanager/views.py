from django.shortcuts import render, redirect
from .forms import addExpenseForm, addEarningForm
from .models import BudgetDetails, ExpenseDetails, EarningDetails


# Create your views here.
def finbalMasterView(request, *args, **kwargs):
    # getting budget details
    budget_details = BudgetDetails.objects.all()
    budgets = []
    budgetAllocated = []
    for head in budget_details:
        budgets.append(str(head.budget.name))
        budgetAllocated.append(head.amount_allocated)

# getting expense Details
    expenses = ExpenseDetails.objects.all()
    headExpenses = []
    for head in budget_details:
        head_expense = expenses.filter(budget_detail=head)
        if(len(head_expense) > 0):
            for expense in head_expense:
                expense_amt = float(expense.amount+expense.tax_amt)
            headExpenses.append(expense_amt)
        else:
            headExpenses.append(0.0)

# getting earning Details
    earnings = EarningDetails.objects.all()
    headEarnings = []
    for head in budget_details:
        head_earning = earnings.filter(budget_detail=head)
        earning_amt = 0
        if(len(head_earning) > 0):
            for earning in head_earning:
                earning_amt = earning_amt+float(earning.amount+earning.tax_amt)
            headEarnings.append(earning_amt)
        else:
            headEarnings.append(0.0)
    totalEarning = 0
    totalExpense = 0
    for earning in headEarnings:
        totalEarning += earning
    print(totalEarning)
    for expense in headExpenses:
        totalExpense += expense
    print(totalExpense)
    profit = totalEarning-totalExpense

    if request.method == 'POST':
        expenseform = addExpenseForm(request.POST)
        earningform = addEarningForm(request.POST)
        if expenseform.is_valid():
            expenseform.save()
            # form_data = expenseform.cleaned_data
            return redirect('/')
        elif earningform.is_valid():
            earningform.save()
            # form_data = earningform.cleaned_data
            return redirect('/')
    else:
        expenseform = addExpenseForm()
        earningform = addEarningForm()
    # print(budgets)
    return render(request, 'home.html', {'expenseform': expenseform,
                                                       'earningform': earningform,
                                                       'budgets': budgets,
                                                       'budgetAllocated': budgetAllocated,
                                                       'headExpenses': headExpenses,
                                                       'headEarnings': headEarnings,
                                                       'totalEarning': totalEarning,
                                                       'totalExpense': totalExpense,
                                                       'profit': profit,
                                                       'earninglist': earnings,
                                                       'expenselist': expenses
                                                       })
