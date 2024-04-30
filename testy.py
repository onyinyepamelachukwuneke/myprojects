import requests
response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=mGY_jfBBhxriPIExHNoKE_biRpfXAKVU")
print (response.status_code)
