#!python
from pprint import pprint
import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)

# Initialise
kws = KiteTicker("5t4uaet9jycxgcmu", "oaK7qBnd0piDCua0xrqKxkzh2D64pYVL")


def on_ticks(ws, ticks):
    # Callback to receive ticks.
    # logging.debug("Ticks: {}".format(ticks))
    pprint(ticks)
    # print(ticks)
    print("\n")


def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([177665, 667468684])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [177665])


# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
