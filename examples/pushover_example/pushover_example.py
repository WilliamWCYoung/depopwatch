from datetime import datetime, timedelta
import time

import pushover
from depopwatch import Listener

import logging
import sys

from settings import settings

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

if __name__ == "__main__":
    #Create a watcher for a depop account
    mary_listen = Listener("maryrosenberger")
    mary_listen.search_account()

    logging.info("Initial scan complete, waiting for new items")

    client = pushover.Client(settings.PUSHOVER_CLIENT_KEY,api_token=settings.PUSHOVER_API_TOKEN)

    while True:
        time.sleep(10)

        #Run in a try/except loop. Doesn't matter, just keep trying!
        try:
            new_items = mary_listen.search_account()

            for item in new_items:
                client.send_message(item,
                                    sound="siren",
                                    title="New depop item!",
                                    priority=2,
                                    expire=datetime.now()+timedelta(days=1),
                                    timestamp=True,
                                    retry=30)

        except Exception as e:
            logging.error(e)
            logging.info("Trying again in 10 seconds")
