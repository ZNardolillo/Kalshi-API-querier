import requests
import datetime
import copy

# This tool retrieves information for a given page on Kalshi.
# As exactly is, it retrieves information for markets relating to the daily temperature high in major cities, but it can be modified for other ones.

# Some general background information: In Kalshi's API, a full city (or any category on the website, really, like rotten tomatoes scores for a movie) is called an "event."
# The individual category bets, like each temperature option, are all called "markets."
# The main thing you need to know to query Kalshi's API is called a "ticker," and is basically an internal ID for each event (and market).

# Fetches the date and concerts it to the proper format for the Kalshi event's full ticker ID
today = datetime.date.today()
months = {
    1: "JAN",
    2: "FEB",
    3: "MAR",
    4: "APR",
    5: "MAY",
    6: "JUN",
    7: "JUL",
    8: "AUG",
    9: "SEP",
    10: "OCT",
    11: "NOV",
    12: "DEC"
}
date = str(today.strftime(f"%y{months[today.month]}%d"))

# These are the city identifying parts of the ticker, which don't change
cities = {
    "Austin": "KXHIGHAUS",
    "Denver": "KXHIGHDEN",
    "Miami": "KXHIGHMIA",
    "New York": "KXHIGHNY",
    "Chicago": "KXHIGHCHI",
    "LA": "KXHIGHLAX",
    "Philadelphia": "KXHIGHPHIL"
}

# Mixes the above two elements to get today's ticker values for each city
full_tickers = copy.deepcopy(cities)
def get_todays_tickers():
    for i in cities:
        full_tickers[i] = f"https://api.elections.kalshi.com/trade-api/v2/events/{cities[i]}-{date}"

# This gets the actual stats of every category for a given city market
def get_current_stats():
    for i in full_tickers:
        url = full_tickers[i]
        response = requests.get(url)
        data = response.json()
        markets = data.get('markets', [])

# If you want more categories other than "no ask," right below this line is where to put them. Take a look at the format of a given page right in an actual web browser to decide which ones you'd like. Here is an example to look over: https://api.elections.kalshi.com/trade-api/v2/events/KXHIGHAUS-25MAY15
        for market in markets:
            print(f"{i} " + market.get('yes_sub_title') + " - no ask: " + str(market.get('no_ask')))

# These are the actual function calls that run the entire script
get_todays_tickers()
get_current_stats()