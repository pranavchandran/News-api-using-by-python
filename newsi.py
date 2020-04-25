from newsapi import NewsApiClient
# from key import my_api_key
import datetime as dt

# newsapi = NewsApiClient(api_key='d784d7159f1a434a9859d80398034d8f')
api_key='d784d7159f1a434a9859d80398034d8f'
newsapi = NewsApiClient(api_key)

# print(type(newsapi))


# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='covid-19',
                                        #   sources='bbc-news,the-verge',
                                        #   category='business',
                                          language='en',
                                          country='in')

# all_articles = newsapi.get_everything(q='covid_19',
#                                     #   sources='bbc-news,the-verge',
#                                     #   domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2020-04-25',
#                                       to='2020-04-25',
#                                       language='en',
#                                     #   country='in',
#                                       sort_by='relevancy',
#                                       page=1)

sources = newsapi.get_sources()

# print(all_articles)
# print(type(top_headlines)) yes class dict
# print(top_headlines.keys()) status totalresults articles
# print(top_headlines['status'])  ok
# print(top_headlines['totalResults']) found=11
# print(type(top_headlines['articles'])) list
# print(top_headlines['articles'][0])

articles = top_headlines['articles']
# for x,y in enumerate(articles):
#     print(f'{x}      {y["title"]}')

# for x,y in enumerate(articles):
#     print(f'{x}      {y["description"]}')

# print(articles)

# for key,value in articles[0].items():
#     print(f'\n{key.ljust(15)} {value}')

for key,value in articles[1].items():
    print(f'\n{key.ljust(15)} {value}')




