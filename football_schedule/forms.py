from django import forms
import calculation
from football_schedule.models import Match


# class CreateBet(forms.Form):
#     bet_amount = forms.FloatField(min_value=1, max_value=10_000)
#     match = forms.ModelChoiceField(queryset=Match.objects.filter(date__startswith='2022-03-19'))


class CreateBet(forms.Form):
    match = forms.ModelChoiceField(queryset=Match.objects.filter(date__startswith='2022-03-20'))
    bet_amount = forms.DecimalField(help_text="Enter amount between 1 and 10_000")
    potential_winnings = forms.DecimalField(
        # widget=calculation.FormulaInput('bet_amount*odds')  # <- using single math expression
    )
