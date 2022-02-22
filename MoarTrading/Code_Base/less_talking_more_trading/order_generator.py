#this file should contain all funcitons necessary to place orders

from .sign_up import client_local
import json
from tda.orders.common import OrderType
from tda.orders.generic import OrderBuilder
from tda.orders.equities import equity_buy_limit
from tda.orders.common import Duration, Session
from .config import acct_id


def order_basic(company_symbol, stock_quantity, price_limit): # we need an equity builder order object to place trades
    
    
    #this is the simples possible order build
        
        # All orders execute during the current normal trading session. If placed outside of trading hours, the execute during the next normal trading session.

        # Time-in-force is set to DAY.

        # All other fields (such as requested destination, etc.) are left unset, meaning they receive default treatment from TD Ameritrade. Note this treatment depends on TDA’s implementation, and may change without warning.


    
    
    #client_local=sign_up.client_local # we need a reference to the local client
    client_local.place_order(
    acct_id,  # account_id
    equity_buy_limit(company_symbol, stock_quantity,price_limit)
        .set_duration(Duration.GOOD_TILL_CANCEL)
        .set_session(Session.SEAMLESS)
        .build())