# Purposes
Generating data from Twitter also known as Company X and apply Stanza sentiment analysis on it.
Keywords for query: 1. "#anzbank" 2. "#anz bank"

# Steps
1. Scraping data about "#anzbank" and "#anz bank" from Twitter by using twscrape library: https://github.com/vladkens/twscrape.
    **twscrape_anz.py**
   Notes: I collected the tweets at 4th September, 2023. Twitter may forbid the usage of twscrape library in the future.
2. Preprocessing data: **preprocess.ipynb**
3. Sentiment analysis by Stanza: **stanza_analysis.ipynb**
4. Visualizing: **visualize.ipynb**
5. Word frequency analysis: **frequency.ipynb**
