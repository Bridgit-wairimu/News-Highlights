from app import app
import datetime
import urllib.request,json
from .models import news

News = news.News

# getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
	'''
	Function that gets the json response to our url request
	'''
	get_news_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['articles']:
			news_result_list = get_news_response['articles']
			news_results = process_newsResults(news_result_list)


	return news_results

def process_newsResults(news_list):
	'''
	Function that processes the news results and transforms them to a list of objects
	'''

	news_results = []
	for news_item in news_list:
		name = news_item.get('name')
		title = news_item.get('title')
		description = news_item.get('description')
		publishedAt = news_item.get('publishedAt')
		content = news_item.get('content')
		url = news_item.get('url')
		urlToImage = news_item.get('urlToImage')

		date_time_obj = datetime.datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
		publishedAt = date_time_obj.date()

		if urlToImage:
			news_object = News(name,title,description,publishedAt,content,url,urlToImage)
			news_results.append(news_object)

	return news_results


def get_news(name):
    get_news_details_url = base_url.format(name,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
			name = news_details_response.get('name')
			title = news_details_response.get('title')
			description = news_details_response.get('description')
			publishedAt = news_details_response.get('publishedAt')
			content = news_details_response.get('content')
			url = news_details_response.get('url')
			urlToImage = news_details_response.get('urlToImage')

            news_object = News(name,title,description,publishedAt,content,url,urlToImage)

    return news_object


def search_news(news_name):
    search_news_url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-29&sortBy=publishedAt&apiKey=0ac1c2d0556d41389f0ea5569f3c85b6'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results



