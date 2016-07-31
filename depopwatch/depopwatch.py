import requests
import re

import logging
logger = logging.getLogger(__name__)

class Listener:
    def __init__(self,username):
        """Initalize a depop watch instance.

        Keyword arguments:
        username -- username of the account you want to watch on Depop
        """

        self.known_items = []
        self.username = username

    def get_current_items(self):
        """Get the current items listed on the given depop account"""

        r = requests.get("https://www.depop.com/en-gb/"+self.username)

        if r.status_code == 200:
            pattern = re.compile(r"""<a class="ProductCard__Link" href="([a-zA-Z\/-]+)">""")
            results = re.findall(pattern ,r.text)
            return results

        return []

    def search_account(self):
        """Seach the given depop account, returning any new items"""

        found_items = self.get_current_items()
        new_items = []

        for item in found_items:
            if item not in self.known_items:
                new_items.append(item)
                self.known_items.append(item)
                logger.info(item)

        return new_items
