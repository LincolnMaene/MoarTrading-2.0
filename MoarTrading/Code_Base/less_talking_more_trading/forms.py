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
    
    company_symbol= forms.CharField()
    stock_quantity= forms.IntegerField()
    price_limit= forms.DecimalField()

class sell_form_basic(forms.Form):
    
    sell_company_symbol= forms.CharField()
    sell_quantity= forms.IntegerField()
    sell_price_limit= forms.DecimalField()
    

class options_form(forms.Form):
    put_or_call=[('PUT', 'p'), ('Call','c')]
    underlying_symbol= forms.CharField()
    expiration_date = forms.DateTimeField()
    contract_type = forms.ChoiceField(choices=put_or_call)
    strike_price_as_string =forms.CharField()
    

