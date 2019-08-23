import pandas as pd

url = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/'

cmc_df = pd.read_html(url)[0]

cmc_df.to_csv('bitcoin.csv')

print(cmc_df)
