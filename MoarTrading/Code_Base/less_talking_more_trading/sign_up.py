#what this file does, essentially, is allow the app to authenticate with tda api
#this file creates the client
from tda import auth, client
import json
from less_talking_more_trading import config 
from less_talking_more_trading import definitions   
api_key=config.api_key 
redirect_uri=config.redirect_uri
token_path=config.token_path

ROOT_DIR=definitions.ROOT_DIR
try:
    client_local = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(ROOT_DIR+'/chromedriver.exe') as driver:#the chromdriver file needs to be found
        client_local = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)


#r = c.get_price_history('AAPL',
#        period_type=client.Client.PriceHistory.PeriodType.YEAR,
#        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#        frequency=client.Client.PriceHistory.Frequency.DAILY)
#assert r.status_code == 200, r.raise_for_status()
#print(json.dumps(r.json(), indent=4))

