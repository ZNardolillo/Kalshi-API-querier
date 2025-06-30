# ReadMe
This tool retrieves information for a given page on Kalshi. The main tool is KalshiDataGrabber.py.
As exactly is, it retrieves information for markets relating to the daily temperature high in major cities, but it can be modified for other ones.

Some general background information: In Kalshi's API, a full city (or any category on the website, really, like rotten tomatoes scores for a movie) is called an "event."
The individual category bets, like each temperature option, are all called "markets."
The main thing you need to know to query Kalshi's API is called a "ticker," and is basically an internal ID for each event (and market).
GetTicker.py can be used to find the ticker for the market you want to query.
