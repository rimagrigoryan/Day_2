#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# %%
# Which url i want to scrape?

url = "https://hetq.am/en"

# %%
# Download the website with requests.get()
r = requests.get(url)

# %%
#lxml =  parser
soup = bs(r.text, "lxml")


# %%
headlines = soup.find_all("h4")

# %%
df = pd.DataFrame(headlines)

#%%df_all = pd.concat()