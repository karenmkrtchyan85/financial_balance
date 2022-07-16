from django.contrib import admin
from .models import Expense,Earning,Budget,ExpenseDetails,EarningDetails,BudgetDetails

# Register your models here.
admin.site.register(Expense)
admin.site.register(Earning)
admin.site.register(Budget)
admin.site.register(ExpenseDetails)
admin.site.register(EarningDetails)
admin.site.register(BudgetDetails)

