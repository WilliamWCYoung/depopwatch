import requests
import re

import logging
logger = logging.getLogger(__name__)

class Listener:
    def __init__(self,username):
        """Initalize a depop watch instance.

            Argument:
            username -- username of the account you want to watch on Depop
            """

        #Insure the username has been provided
        assert isinstance(username, str)

        #Insure the username exists on Depop
        r = requests.get("https://www.depop.com/en/"+username)

        #Will throw a 404 if account doesn't exist
        assert r.status_code == 200

        self.known_items = []
        self.username = username

    def _get_current_items(self):
        """Get the current items listed on the given depop account."""
       
        r = requests.get("https://www.depop.com/en/"+self.username)

        if r.status_code == 200:
            pattern = re.compile(r"""<a class="ProductCard__Link" href="([a-zA-Z\/-]+)">""")
            results = re.findall(pattern ,r.text)
            return results

        return []

    def search_account(self):
        """Seach the given depop account, returning any new items.

            Example:
            >>> listener.search_account()
            ["/en-gb/maryrosenberger/mary-rosenberger-the-power-in",...]
            """

        found_items = self._get_current_items()
        new_items = []

        for item in found_items:
            if item not in self.known_items:
                new_items.append(item)
                self.known_items.append(item)
                logger.info(item)

        return new_items
