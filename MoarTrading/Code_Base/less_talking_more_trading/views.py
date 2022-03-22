from asyncio.windows_events import NULL
import datetime
import email
from pickle import NONE
from this import d
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import(form_example, order_form_basic, sell_form_basic, options_form, options_query_form,
    order_trigger_form, sale_trigger_form, Market_Query_Form, Movers_Query_Form
)
from .order_generator import order_basic, one_order_triggers_another, options_order_single, generate_buy_equity_order
from .sell_generator import sell_basic, generate_sell_equity_order,sale_order_triggers_another
from .market_hours_generator import single_market_hours
from .option_chains_generator import generate_options_calls_date, generate_options_put_date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .movers_generator import get_movers
import json


# #example for how to access user profile in function based view
    # u = User.objects.get(username=request.user.username)
    # tda_id = u.profile.tdameritrade_id


   

    # print(acct_id)

    #for class based views use: self.request.user.username



#these lines essentiall fill the options_query object with junk data so function knows what type it is
trial_start_date=datetime.datetime.strptime('2022-2-22', '%Y-%m-%d').date()
trial_end_date=datetime.datetime.strptime('2022-2-22', '%Y-%m-%d').date()

options_query_object=generate_options_calls_date('GOOG', 300 , trial_start_date, trial_end_date) #this will hold query data for option chains
hours_query_object=single_market_hours('EQUITY',trial_end_date)#this will hold query data for market hours chains
movers_query_obj=NONE
#setup for options query object ends here

class Movers_data_view (APIView): #this should give the user the top ten movers for that day and so on and so forth

    authentication_classes=[]
    permission_classes=[]

    list_of_lists=[[]] * 10

    list_of_descriptions=[[]] * 10

    list_of_symbols=[[]] * 10

    def get(self,request, format=None):
        

        for x in range(0, 10):

            Movers_data_view.list_of_lists[x]=list(movers_query_obj[x].items())

        for x in range(0, 10):

            Movers_data_view.list_of_descriptions[x]=list(Movers_data_view.list_of_lists[x][1])

        for x in range(0, 10):

            Movers_data_view.list_of_symbols[x]=list(Movers_data_view.list_of_lists[x][4])

        for x in range(0, 10):

            Movers_data_view.list_of_symbols[x]=str(Movers_data_view.list_of_symbols[x])
            Movers_data_view.list_of_descriptions[x]=str(Movers_data_view.list_of_descriptions[x])
       
       
       #by the time we reach here, i have converted the symbols and company names into usable strings for html

        print(Movers_data_view.list_of_symbols)
        # for x in jsonObject:
        return Response(movers_query_obj)    #     print(x)

          

class Movers_Query_view(FormView):

    

    template_name='movers_query.html'

    form_class=Movers_Query_Form

    success_url='/movers_data'


    def form_valid(self, form):

        global movers_query_obj

        global hours_query_object #without this python just creates a local var
        

        index=form.cleaned_data['index']
        direction=form.cleaned_data['direction']#GET compay 1 daTA
        change=form.cleaned_data['change']
       
       
       

        movers_query_obj=get_movers(index,direction,change)

        # print(index)

    





        

        return super().form_valid(form)


class Market_hours_view (APIView):

    authentication_classes=[]
    permission_classes=[]

    def get(self,request, format=None):

        is_open=False#tells us if the market is open
        


        #print(options_query_object)

        # data={

        #     "sales":177,
        #     "customers":120,
        # }
       
        jsonObject = list(hours_query_object.items()) #this shenanigan is supposed to extract the nested dictio i want into a json object list
        needed_string=jsonObject[0][1]
        jsonObject=list(needed_string.items())
        needed_string=jsonObject[0][1]
        jsonObject=list(needed_string.items())

    
        if(jsonObject[6][1]==True):#if the stock market is open, we know
            is_open=True

        if is_open==True: #if market is open
            needed_string=jsonObject[7][1]
            jsonObject=list(needed_string.items())

        # for x in jsonObject:
        #     print(x)

            pre_market=jsonObject[0]
            regular_market=jsonObject[1]
            post_market=jsonObject[2]

            title, pre_market_data=pre_market #this transfors all the data needed to a string

            pre_market_data=list(pre_market)
            pre_market_data=pre_market_data[1]
            
            pre_market_data=str(pre_market_data)

            title, reg_market_data=regular_market

            reg_market_data=list(regular_market)
            reg_market_data=reg_market_data[1]
            
            reg_market_data=str(reg_market_data)

            title, post_market_data=post_market

            post_market_data=list(post_market)
            post_market_data=post_market_data[1]
            
            post_market_data=str(post_market_data)
            disallowed_characters="{[]}'"
            for ch in disallowed_characters:
                pre_market_data=pre_market_data.replace(ch,"")
                reg_market_data=reg_market_data.replace(ch,"")
                post_market_data=post_market_data.replace(ch,"")
                

            data=[is_open,pre_market_data,reg_market_data,post_market_data]

            # print(pre_market_data)
            
            return render(request, 'market_hrs.html', {'data': data})
        
        return render(request, 'maket_closed_err.html')

        

class Market_Query_view(FormView):

    

    template_name='market_hours_query.html'

    form_class=Market_Query_Form

    success_url='/market_hours'


    def form_valid(self, form):

        global hours_query_object #without this python just creates a local var
        

        Market=form.cleaned_data['Market']
        Year=form.cleaned_data['Year']#GET compay 1 daTA
        Month=form.cleaned_data['Month']
        Day=form.cleaned_data['Day']#GET compay 1 daTA
        Hour=form.cleaned_data['Hour']
        Minutes=form.cleaned_data['Minutes']#GET compay 1 daTA
       
        
        date_maker = datetime.datetime(Year, Month, Day, Hour, Minutes)

        hours_query_object=single_market_hours(Market, date_maker)

        # print(date_maker)

        

    





        

        return super().form_valid(form)


class sale_trigger_sale_view(FormView):

    template_name='one_sale_triggers_another.html'

    form_class=sale_trigger_form

    success_url='/home'


    def form_valid(self, form):

        username_query=self.request.user.username #get id of logged in user 

        logged_in_user =  User.objects.get(username=username_query) #get user object

        tda_id = logged_in_user.profile.tdameritrade_id #get user ameritrade id

        


        company_1_symbol=form.cleaned_data['company_1_symbol']#GET compay 1 daTA
        stock_1_quantity=form.cleaned_data['stock_1_quantity']
        price_1_limit=form.cleaned_data['price_1_limit']

        company_2_symbol=form.cleaned_data['company_2_symbol']#GET compay 2 daTA
        stock_2_quantity=form.cleaned_data['stock_2_quantity']
        price_2_limit=form.cleaned_data['price_2_limit']
        timing=form.cleaned_data['timing'] #useless better to replace with choice between trigger cancel and trigger order
        session=form.cleaned_data['session']  #useless better to replace with choice between trigger cancel and trigger order

        order_1=generate_sell_equity_order(company_1_symbol, stock_1_quantity, price_1_limit)
        order_2=generate_sell_equity_order(company_2_symbol, stock_2_quantity, price_2_limit)

        sale_order_triggers_another(tda_id, order_1, order_2)

        #print(company_1_symbol,stock_1_quantity, price_1_limit, company_2_symbol,stock_2_quantity, price_2_limit)

    





        

        return super().form_valid(form)


class order_trigger_order_view(FormView):

    template_name='one_order_trig_another.html'

    form_class=order_trigger_form

    success_url='/home'


    def form_valid(self, form):

        username_query=self.request.user.username #get id of logged in user 

        logged_in_user =  User.objects.get(username=username_query) #get user object

        tda_id = logged_in_user.profile.tdameritrade_id #get user ameritrade id

        


        company_1_symbol=form.cleaned_data['company_1_symbol']#GET compay 1 daTA
        stock_1_quantity=form.cleaned_data['stock_1_quantity']
        price_1_limit=form.cleaned_data['price_1_limit']

        company_2_symbol=form.cleaned_data['company_2_symbol']#GET compay 2 daTA
        stock_2_quantity=form.cleaned_data['stock_2_quantity']
        price_2_limit=form.cleaned_data['price_2_limit']
        timing=form.cleaned_data['timing']  #useless better to replace with choice between trigger cancel and trigger order
        session=form.cleaned_data['session'] #useless better to replace with choice between trigger cancel and trigger order

        order_1=generate_buy_equity_order(company_1_symbol, stock_1_quantity, price_1_limit)
        order_2=generate_buy_equity_order(company_2_symbol, stock_2_quantity, price_2_limit)

        one_order_triggers_another(tda_id, order_1, order_2)

        #print(company_1_symbol,stock_1_quantity, price_1_limit, company_2_symbol,stock_2_quantity, price_2_limit)

    





        

        return super().form_valid(form)


class options_view(FormView):

    template_name='options_order.html'

    form_class=options_form

    success_url='/home'


    def form_valid(self, form):

        username_query=self.request.user.username #get id of logged in user 

        logged_in_user =  User.objects.get(username=username_query) #get user object

        tda_id = logged_in_user.profile.tdameritrade_id #get user ameritrade id
        
        underlying_symbol=form.cleaned_data['underlying_symbol']
        quantity=form.cleaned_data['quantity']
        
        #print(underlying_symbol, expiration_date, contract_type, strike_price_as_string)

        options_order_single(underlying_symbol,quantity, tda_id)



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
        
        username_query=self.request.user.username #get id of logged in user 

        logged_in_user =  User.objects.get(username=username_query) #get user object

        tda_id = logged_in_user.profile.tdameritrade_id #get user ameritrade id

        # print('acct id: ')
        # print(tda_id)




        company_symbol=form.cleaned_data['company_symbol']
        stock_quantity=form.cleaned_data['stock_quantity']
        price_limit=form.cleaned_data['price_limit']
        timing=form.cleaned_data['timing']
        session=form.cleaned_data['session']

        order_basic(company_symbol, stock_quantity, price_limit, timing, session, tda_id)

        # same for all other fields, can also do form.save() if model form


        

        return super().form_valid(form)


class basic_sell_view(FormView):

    template_name='basic_sell.html'

    form_class=sell_form_basic

    success_url='/home'


    def form_valid(self, form):
        
        username_query=self.request.user.username #get id of logged in user 

        logged_in_user =  User.objects.get(username=username_query) #get user object

        tda_id = logged_in_user.profile.tdameritrade_id #get user ameritrade id
       
        company_symbol=form.cleaned_data['sell_company_symbol']
        stock_quantity=form.cleaned_data['sell_quantity']
        price_limit=form.cleaned_data['sell_price_limit']
        timing=form.cleaned_data['timing']
        session=form.cleaned_data['session']

        sell_basic(company_symbol, stock_quantity, price_limit, timing, session, tda_id)

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
