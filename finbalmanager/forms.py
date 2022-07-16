from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import ExpenseDetails, EarningDetails


class addExpenseForm(ModelForm):
    class Meta():
        model = ExpenseDetails
        fields = ['budget_detail', 'expense', 'amount', 'tax_amt', 'date',
                  'invoice_no', 'order_ref_no', 'trn_ref_no', 'comments']


class addEarningForm(ModelForm):
    class Meta():
        model = EarningDetails
        fields = ['budget_detail', 'earning', 'amount', 'tax_amt', 'date',
                  'invoice_no', 'order_ref_no', 'trn_ref_no', 'comments']
