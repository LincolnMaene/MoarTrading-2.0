import sign_up
import json


client_local=sign_up.client_local

def generate_options(stock_symbol):#takes in stock symbol and returns all stock options json
  response = client_local.get_option_chain(stock_symbol) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))


def generate_options_calls(stock_symbol):#takes in stock symbol and returns call stock options json
  response = client_local.get_option_chain(stock_symbol, contract_type=client_local.Options.ContractType.CALL) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))

def generate_options_calls_strike(stock_symbol, strike_number):#takes in stock symbol and returns call stock options json
  response = client_local.get_option_chain(stock_symbol, contract_type=client_local.Options.ContractType.CALL, strike=strike_number) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))

def generate_options_put(stock_symbol):#takes in stock symbol and returns put stock options json
  response = client_local.get_option_chain(stock_symbol, contract_type=client_local.Options.ContractType.PUT) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))

def generate_options_put_strike(stock_symbol, strike_number):#takes in stock symbol and returns call stock options json
  response = client_local.get_option_chain(stock_symbol, contract_type=client_local.Options.ContractType.PUT, strike=strike_number) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))

def generate_options_calls_date(stock_symbol, strike_number, date_from, date_to):#takes in stock symbol and returns call stock options json
  response = client_local.get_option_chain(stock_symbol, contract_type=client_local.Options.ContractType.CALL, strike=strike_number, from_date=date_from, to_date=date_to) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))

def generate_options_put_date(stock_symbol, strike_number,  date_from, date_to):#takes in stock symbol and returns put stock options json
  response = client_local.get_option_chain(stock_symbol, contract_type=client_local.Options.ContractType.PUT, strike=strike_number, from_date=date_from, to_date=date_to) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))