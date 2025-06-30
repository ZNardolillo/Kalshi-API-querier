import requests
import datetime
from datetime import timedelta

# This tool finds the ticker ID for a given market. Search the following copied line and edit the one directly
# beneath it to find your desired market:

# ~~~# The line right below this one is where you write what category you want to search~~~

# This takes a little bit of time to run. Some print statements are really more for piece of mind for the user
# that the tool is still working and hasn't been caught in an infinite loop, but you can safely disable them.

class Big_Query:
    today = datetime.date.today()
    yesterday = today - timedelta(days=1)
    # yesterday tells the program when to stop querying.
    # Kalshi tends to have open markets relevant to both today and tomorrow, so there will likely be some duplicates
    # from all of this. Since all markets aren't necessarily added at the same time, this is more exhaustive and safe.
    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    # Reformats the date into the form its found in tickers
    yesterday = yesterday.strftime(f"{months[yesterday.month]} {yesterday.day}")

    def initialization(self):
        self.cursor = 1
        self.headers = {"accept": "application/json"}
        self.more_data = True
        self.page_count = 0  # Track how many pages we've loaded
        self.match_count = 0

    def query_one_page(self):
        if not self.more_data:
            return

        # Note that all of Kalshi's API uses this url with "elections" in it, even for markets
        # that have nothing to do with elections. I assume their tool used to be more specific
        # and came to encompass all of their different markets later on.
        url = f"https://api.elections.kalshi.com/trade-api/v2/markets?cursor={self.cursor}"
        response = requests.get(url, headers=self.headers)

        data = response.json()
        markets = data.get('markets', [])

        self.page_count += 1
        print(f"Queried page {self.page_count}, got {len(markets)} markets")

        for market in markets:
            # The line right below this one is where you write what category you want to search
            if "temp" in market.get('title'):
                print(market.get('ticker') + " " + market.get('title'))
                self.match_count += 1
            if self.yesterday in market.get('title'):
                print("Reached old data - terminating")
                self.more_data = False
                break

        print(f"Total matches so far: {self.match_count}")

        self.cursor = data.get("cursor")
        if not self.cursor:
            self.more_data = False

x = Big_Query()
x.initialization()

while x.more_data == True:
    x.query_one_page()