import pandas as pd

data = pd.read_csv("../data/yelp_business.csv")

print(data.latitude.max())
print(data.latitude.min())
print(data.longitude.max())
print(data.longitude.min())

# Random generate 100 points
sample = data.sample(n=10000)

sample = sample[['latitude', 'longitude']]

sample.to_csv('../data/sample_10000.csv', index=False, header=None)
