from session import token, fyers


def optionBuyOrder(symbol):
    #   NSE:BANKNIFTY20N0525000PE
    data = { "symbol":symbol,
        "qty":25,
        "type":2,  
        "side":1,                        # 1 => Buy   -1 => Sell
        "productType":"INTRADAY",   
        "limitPrice":0,
        "stopPrice":0 ,
        "disclosedQty":0, 
        "validity":"DAY", 
        "offlineOrder":"False", 
        "stopLoss":0,  
        "takeProfit":0
    }

    return fyers.place_orders(token, data)
    
def optionSellOrder(symbol):
    #NSE:BANKNIFTY20N0525000PE
    data = { "symbol":symbol,
        "qty":25,
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

    return fyers.place_orders(token, data)