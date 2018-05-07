import pandas as pd

data = pd.read_csv("../data/yelp_business.csv")

data_needed = data[['business_id', 'name', "stars", "categories", "latitude", "longitude"]]

data_needed.to_csv('../data/yelp_business_min.csv', index=False)
