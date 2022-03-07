from unicodedata import category
from django import forms
from crispy_forms.helper import FormHelper


Exaxmple_Choices=[('question', 'Question'), ('other','Other')]

class form_example(forms.Form):

    helper=FormHelper()

    #helper.form_show_labels=False
    
    name= forms.CharField()
    email= forms.EmailField(label="E-Mail")
    category=forms.ChoiceField(choices=Exaxmple_Choices)
    subject=forms.CharField (required=False)
    body = forms.CharField(widget=forms.Textarea)


class order_form_basic(forms.Form):
    timing=[('Day', 'day'), ('Good Till Cancel','good till cancel'), ('Fill or Kill','fill or kill')]
    company_symbol= forms.CharField()
    stock_quantity= forms.IntegerField()
    price_limit= forms.DecimalField()
    timing = forms.ChoiceField(choices=timing)

class sell_form_basic(forms.Form):
    
    sell_company_symbol= forms.CharField()
    sell_quantity= forms.IntegerField()
    sell_price_limit= forms.DecimalField()
    

class options_form(forms.Form):
   
    underlying_symbol= forms.CharField()
    quantity=forms.IntegerField()
    
class options_query_form(forms.Form):
    put_or_call=[('PUT', 'p'), ('Call','c')]
    underlying_symbol= forms.CharField()
    start_date = forms.DateTimeField()
    strike_number=forms.IntegerField()
    end_date = forms.DateTimeField()
    contract_type = forms.ChoiceField(choices=put_or_call)

