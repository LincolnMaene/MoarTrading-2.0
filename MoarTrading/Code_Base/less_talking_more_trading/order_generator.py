#this file should contain all funcitons necessary to place orders

from datetime import datetime
from .sign_up import client_local
import json
from tda.orders.common import OrderType
from tda.orders.generic import OrderBuilder
from tda.orders.equities import equity_buy_limit
from tda.orders.common import Duration, Session
from .config import acct_id
from tda.orders.options import OptionSymbol, option_buy_to_open_market


def order_basic(company_symbol, stock_quantity, price_limit, timing): # we need an equity builder order object to place trades
    
    
    #this is the simples possible order build
        
        # All orders execute during the current normal trading session. If placed outside of trading hours, the execute during the next normal trading session.

        # Time-in-force is set to DAY.

        # All other fields (such as requested destination, etc.) are left unset, meaning they receive default treatment from TD Ameritrade. Note this treatment depends on TDA’s implementation, and may change without warning.
    
    duration=Duration.GOOD_TILL_CANCEL
    if(timing=='Day'):
        duration=Duration.DAY
    elif (timing=='Fill or Kill'):
        duration=Duration.FILL_OR_KILL


    
    
    #client_local=sign_up.client_local # we need a reference to the local client
    client_local.place_order(
    acct_id,  # account_id
    equity_buy_limit(company_symbol, stock_quantity,price_limit)
        .set_duration(duration)
        .set_session(Session.SEAMLESS)
        .build())

def obtain_options_symbol(company_symbol, exp_year, exp_month, exp_day, put_call, strike_price):

    options_symbol=OptionSymbol(
    company_symbol, datetime.date(year=exp_year, month=exp_month, day=exp_day), put_call, strike_price).build()

    return options_symbol


def options_order_single(company_symbol, stock_quantity): # we need an equity builder order object to place trades
    
    
    #this is the simples possible options order
    #had to hunt down some chinese website to figure out the documentation
        
        
        

    print('trying to order options for ',company_symbol)
    
    #client_local=sign_up.client_local # we need a reference to the local client
    client_local.place_order(
    acct_id,  # account_id
    option_buy_to_open_market(company_symbol, stock_quantity)
        )

