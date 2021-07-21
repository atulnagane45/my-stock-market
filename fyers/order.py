from fyers_api import fyersModel
access_token = 'gAAAAABg7_w4YT-3EEFuIcL8SO9yXhnpJCqlhc4QC4nxzE0TWzRVh6FQ7Hu6KDwfgvkSHNRJgZ_mlZP89HTMEV41vq2n4l7zqCpKbRXUBqbJCbwLQRO2FJc=&user_id=XA08240&poa_flag=N'
token = access_token

is_async = False #(By default False, Change to True for asnyc API calls.)

fyers = fyersModel.FyersModel(is_async)

def buyOrder():
    #   NSE:BANKNIFTY20N0525000PE
    data = { "symbol":"NSE:BANKNIFTY20N0525000PE",
        "qty":1,
        "type":2,  
        "side":1, 
        "productType":"INTRADAY",   
        "limitPrice":0,
        "stopPrice":0 ,
        "disclosedQty":0, 
        "validity":"DAY", 
        "offlineOrder":"False", 
        "stopLoss":0,  
        "takeProfit":0
    }

    return fyers.place_basket_orders(data)
    
def sellOrder():
    #   NSE:BANKNIFTY20N0525000PE
    data = { "symbol":"NSE:BANKNIFTY20N0525000PE",
        "qty":1,
        "type":2,  
        "side":-1,                                     # 1 => Buy   -1 => Sell
        "productType":"INTRADAY",   
        "limitPrice":0,
        "stopPrice":0 ,
        "disclosedQty":0, 
        "validity":"DAY", 
        "offlineOrder":"False", 
        "stopLoss":0,  
        "takeProfit":0
    }

    return fyers.place_basket_orders(data)