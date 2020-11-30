from flask import render_template,request,redirect,url_for
from  .import main
from ..requests import get_news,get_sources


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    category_news = get_news('category_news')
    sources_news = get_sources()

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, category = category_news,sources = sources_news)


