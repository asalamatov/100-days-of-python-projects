STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_API_KEY = "FT208AHHQ0T5Q51B"
NEWS_API_KEY = "00f05a3bae61406fa8d87befb4b8ae7b"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={STOCK_NAME}&apikey={ALPHA_API_KEY}'
r = requests.get(url)
data = r.json()['Weekly Time Series']
data_list = [v for (k,v) in data.items()]

this_week_data = data_list[0]
previous_week_data = data_list[1]

print(this_week_data)
print(previous_week_data)
#TODO 2. - Get the day before yesterday's closing stock price
this_week_closing = float(this_week_data['4. close'])
previous_week_closing = float(previous_week_data['4. close'])
print()
print(this_week_closing)
print(previous_week_closing)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_between_two_weeks_stocks = abs(this_week_closing-previous_week_closing)
print(difference_between_two_weeks_stocks)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference_between_two_weeks_stocks = difference_between_two_weeks_stocks/this_week_closing*100
print(percentage_difference_between_two_weeks_stocks)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if (percentage_difference_between_two_weeks_stocks>5):
    print("Great News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
url_news = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
r_news = requests.get(url_news)
data_news = r_news.json()['articles'][0:3]

last_3_news_about_Tesla = dict()

for i in range(3):
    last_3_news_about_Tesla[data_news[i]["title"]] = data_news[0]["url"]

print(data_news[0]["title"])
print(data_news[0]["url"])
print(last_3_news_about_Tesla)

for k,v in last_3_news_about_Tesla.items():
    print(k, "\n >>>>", v , "\n")
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

