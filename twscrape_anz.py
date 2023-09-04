import asyncio
from twscrape import API
import pandas as pd

async def main():
    # default: accounts will be added into accounts.db
    api = API("accounts.db")
    
    # ADD ACCOUNTS (for CLI usage see BELOW)
    # await api.pool.delete_accounts(usernames="")
    # await api.pool.add_account("username", "password", "email address", "pwd of your email")
    # relogin to your twitter
    await api.pool.relogin(usernames="bai_miranda")
    # Set the account as active
    await api.pool.set_active("bai_miranda",active=True)
    
    # equals to in `explore` search the keywords and click 'latest' in Twitter APP
    # 1. "#anzbank" 2. "#anz bank"
    q = "#anz bank"
    tweets_data = []
    async for tweet in api.search(q, limit=5000):
        # print(tweet)
        print("extracting......")
        # Convert datetime to timezone-unaware format
        tweets_data.append([tweet.id_str, tweet.date.date(), tweet.date.tzname(), tweet.lang, tweet.rawContent, tweet.url, tweet.hashtags, tweet.mentionedUsers, tweet.place])
    
    df = pd.DataFrame(tweets_data)
    # export data to excel sheet
    df.to_excel("./data/twscrape2.xlsx")

if __name__ == "__main__":
    asyncio.run(main())