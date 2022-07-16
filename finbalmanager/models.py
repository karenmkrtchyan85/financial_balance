from django.db import models
# from .models import ExpenseDetails,EarningDetails
# from .models import BudgetDetails
# Create your models here.


class Budget(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)

    def __str__(self):
        # +'_'+str(self.budget_desc)
        # return f'Budget name={self.name}'
        return f'(Budget {self.name})'


class Expense(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)

    def __str__(self):
        # +'_'+str(self.expense_desc)
        # return f'Expense name={self.name}'
        return f'(Expense {self.name})'


class Earning(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)

    def __str__(self):
        # +'_'+str(self.expense_desc)
        # return f'Earning name={self.name}'
        return f'(Earning {self.name})'


class BudgetDetails(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, default=1)
    amount_allocated = models.FloatField()
    start_date = models.DateField()
    amount_used = models.FloatField()
    amount_surplus = models.FloatField()
#    expenses=models.ManyToManyField(ExpenseDetails)
#    earnings=models.ManyToManyField(EarningDetails)
    comments = models.TextField(max_length=500)

    def __str__(self):
        return f'(BudgetDetails {self.budget} + _FY_ + {self.start_date})'


class ExpenseDetails(models.Model):
    budget_detail = models.ForeignKey(
        BudgetDetails, on_delete=models.CASCADE, default=1)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, default=1)
    amount = models.FloatField(default=0.00)
    tax_amt = models.FloatField(default=0.00)
    date = models.DateField()
    invoice_no = models.CharField(max_length=50, blank=True)
    order_ref_no = models.CharField(max_length=50, blank=True)
    trn_ref_no = models.CharField(max_length=50, blank=True)
    comments = models.CharField(max_length=500)

    def __str__(self):
        return f'(ExpenseDetails {self.budget_detail} + _ + {self.expense}'


class EarningDetails(models.Model):
    budget_detail = models.ForeignKey(
        BudgetDetails, on_delete=models.CASCADE, default=1)
    earning = models.ForeignKey(Earning, on_delete=models.CASCADE, default=1)
    amount = models.FloatField(default=0.00)
    tax_amt = models.FloatField(default=0.00)
    date = models.DateField()
    invoice_no = models.CharField(max_length=50, blank=True)
    order_ref_no = models.CharField(max_length=50, blank=True)
    trn_ref_no = models.CharField(max_length=50, blank=True)
    comments = models.CharField(max_length=500)

    def __str__(self):
        # return f"EarningDetails {self.budget_detail} '_' {self.earning}"
        return f'(EarningDetails {self.budget_detail} + _ + {self.earning}'
