# Purposes
Generating data from Twitter also known as Company X and apply Stanza sentiment analysis on it.
Keywords for query: 1. "#anzbank" 2. "#anz bank"

# Steps
1. Scraping data about "#anzbank" and "#anz bank" from Twitter by using twscrape library: https://github.com/vladkens/twscrape.
    **twscrape_anz.py**
Notes: I collected the tweets at 4th September, 2023. Twitter may forbid the usage of twscrape library in the future.
3. Preprocessing data: **preprocess.ipynb**
4. Sentiment analysis by Stanza: **stanza_analysis.ipynb**
5. Visualizing: **visualize.ipynb**
6. Word frequency analysis: **frequency.ipynb**
