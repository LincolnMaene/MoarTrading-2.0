import email
from this import d
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import form_example, order_form_basic, sell_form_basic, options_form
from .order_generator import order_basic
from .sell_generator import sell_basic



class form_example_view(FormView):

    # we grab the model form
    
   
    template_name='form_example.html'

    form_class=form_example

    success_url='/home'


    def form_valid(self, form):
        
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']

        

        # same for all other fields, can also do form.save() if model form


        print(name, email)

        return super().form_valid(form)


class options_view(FormView):

    template_name='options_order.html'

    form_class=options_form

    success_url='/home'


    def form_valid(self, form):
        
        underlying_symbol=form.cleaned_data['underlying_symbol']
        expiration_date=form.cleaned_data['expiration_date']
        contract_type=form.cleaned_data['contract_type']
        strike_price_as_string=form.cleaned_data['strike_price_as_string']

        print(underlying_symbol, expiration_date, contract_type, strike_price_as_string)

        # same for all other fields, can also do form.save() if model form


        

        return super().form_valid(form)

class basic_order_view(FormView):

    template_name='basic_order.html'

    form_class=order_form_basic

    success_url='/home'


    def form_valid(self, form):
        
        company_symbol=form.cleaned_data['company_symbol']
        stock_quantity=form.cleaned_data['stock_quantity']
        price_limit=form.cleaned_data['price_limit']

        order_basic(company_symbol, stock_quantity, price_limit)

        # same for all other fields, can also do form.save() if model form


        

        return super().form_valid(form)


class basic_sell_view(FormView):

    template_name='basic_sell.html'

    form_class=sell_form_basic

    success_url='/home'


    def form_valid(self, form):
        
       
        company_symbol=form.cleaned_data['sell_company_symbol']
        stock_quantity=form.cleaned_data['sell_quantity']
        price_limit=form.cleaned_data['sell_price_limit']

        sell_basic(company_symbol, stock_quantity, price_limit)

        # same for all other fields, can also do form.save() if model form


       

        return super().form_valid(form)






    
    


    

    

class home_view(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'home.html', {})


class data_test_view (APIView):

    authentication_classes=[]
    permission_classes=[]

    def get(self,request, format=None):
        data={

            "sales":100,
            "customers":10,
        }
        return Response(data)

