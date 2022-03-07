from asyncio.windows_events import NULL
import datetime
import email
from this import d
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import form_example, order_form_basic, sell_form_basic, options_form, options_query_form
from .order_generator import order_basic, obtain_options_symbol, options_order_single
from .sell_generator import sell_basic
from .option_chains_generator import generate_options_calls_date, generate_options_put_date



#these lines essentiall fill the options_query object with junk data so function knows what type it is
trial_start_date=datetime.datetime.strptime('2022-2-22', '%Y-%m-%d').date()
trial_end_date=datetime.datetime.strptime('2022-2-22', '%Y-%m-%d').date()

options_query_object=generate_options_calls_date('GOOG', 300 , trial_start_date, trial_end_date) #this will hold query data for option chains

#setup for options query object ends here
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
        quantity=form.cleaned_data['quantity']
        
        #print(underlying_symbol, expiration_date, contract_type, strike_price_as_string)

        options_order_single(underlying_symbol,quantity)



        # same for all other fields, can also do form.save() if model form





        

        return super().form_valid(form)

class options_query_view(FormView): #this view is repsonsible for giving us a query of options data

    template_name='options_query.html'

    form_class=options_query_form

    success_url='/options_data'


    def form_valid(self, form):
        
        global options_query_object#without global, python will just create a local variable

        underlying_symbol=form.cleaned_data['underlying_symbol']
        end_date=form.cleaned_data['end_date']
        start_date=form.cleaned_data['start_date']
        strike_number=form.cleaned_data['strike_number']
        contract_type=form.cleaned_data['contract_type']

        #print(underlying_symbol, expiration_date, contract_type, strike_price_as_string)

        # start_date=datetime.datetime.strptime('2022-2-22', '%Y-%m-%d').date()
        # end_date=datetime.datetime.strptime('2023-12-31', '%Y-%m-%d').date()



        # same for all other fields, can also do form.save() if model form

        if(contract_type=='Call'):
            options_query_object=generate_options_calls_date(underlying_symbol, strike_number , start_date, end_date)
        else:
            options_query_object=generate_options_put_date(underlying_symbol, strike_number , start_date, end_date)

        #print(options_query_object)




        

        return super().form_valid(form)


    

class basic_order_view(FormView):

    template_name='basic_order.html'

    form_class=order_form_basic

    success_url='/home'


    def form_valid(self, form):
        
        company_symbol=form.cleaned_data['company_symbol']
        stock_quantity=form.cleaned_data['stock_quantity']
        price_limit=form.cleaned_data['price_limit']
        timing=form.cleaned_data['timing']

        order_basic(company_symbol, stock_quantity, price_limit, timing)

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


class options_data_view (APIView):

    authentication_classes=[]
    permission_classes=[]

    def get(self,request, format=None):

        #print(options_query_object)

        # data={

        #     "sales":177,
        #     "customers":120,
        # }
        return Response(options_query_object)


