#using panda
import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')
print(len(df))
print(df[2])
df[2].to_csv('top_billionaires.csv')