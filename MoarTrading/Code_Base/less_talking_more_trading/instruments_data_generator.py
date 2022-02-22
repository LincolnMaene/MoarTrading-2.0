import sign_up
import json

c_local=sign_up.client_local #makes it so i don't have to reuse c

def search_instruments(company_symbol):#return instrument data, including fundamental analyis data, uses list of symbols
    response=c_local.search_instruments([company_symbol], c_local.Instrument.Projection.FUNDAMENTAL)
    print(json.dumps(response.json(), indent=4))
