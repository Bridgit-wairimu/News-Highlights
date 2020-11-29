from app import app
import datetime
import urllib.request,json
from .models import news,sources

News = news.News
Sources = sources.Sources


# getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# Getting the sources base url
sources_base_url = app.config["NEWS_SOURCE_BASE_URL"]

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
		author = news_item.get('author')
		title = news_item.get('title')
		description = news_item.get('description')
		publishedAt = news_item.get('publishedAt')
		content = news_item.get('content')
		url = news_item.get('url')
		urlToImage = news_item.get('urlToImage')

		date_time_obj = datetime.datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
		publishedAt = date_time_obj.date()

		if urlToImage:
			news_object = News(author,title,description,publishedAt,content,url,urlToImage)
			news_results.append(news_object)

	return news_results


def get_sources():
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = sources_base_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['articles']:
			sources_result_list = get_sources_response['articles']
			sources_results = process_sourcesResults(sources_result_list)


	return sources_results

def process_sourcesResults(sources_list):
	'''
	Function that processes the sources results and transforms them to a list of objects
	'''

	sources_results = []
	for source_item in sources_list:
		id = source_item.get('id')
		name = source_item.get('name')

		source_object = Sources(id,name)
		sources_results.append(source_object)

	return sources_results
