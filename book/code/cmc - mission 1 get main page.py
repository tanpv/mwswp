import pandas as pd

cmc_df = pd.read_html('https://coinmarketcap.com/')
cmc_export = cmc_df[0][['#','Name','Market Cap','Price','Volume (24h)','Circulating Supply','Change (24h)']]
cmc_export.to_csv('cmc_main.csv', index=False)

print(cmc_export.columns)
print(cmc_export)

