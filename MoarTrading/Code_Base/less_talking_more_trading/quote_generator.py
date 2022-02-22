import sign_up
import json

def generate_quote(stock_symbol):#takes in stock symbol and returns quote json
  response = sign_up.client_local.get_quotes(stock_symbol) # get quotes for Boeing company
  print (json.dumps(response.json(),indent=4))








