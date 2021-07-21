#!python
from pprint import pprint

from kiteconnect import KiteTicker

kws = KiteTicker("sp9kkdub3kf8qufe", "8ZN453ZmcAlTNSOWSxSaPPhhBmJ6ZQk3")


def on_ticks(ws, ticks):
    # Callback to receive ticks.
    # logging.debug("Ticks: {}".format(ticks))
    pprint(ticks)
    # print(ticks)
    print("\n")


def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([3050241, 177665])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [3050241, 177665])


# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
