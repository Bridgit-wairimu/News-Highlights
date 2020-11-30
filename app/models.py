class News:
    """ News class to define the articles object 
    """

    def __init__(self, author, title, description,publishedAt,content,url,urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.urlToImage = urlToImage
        self.url = url


class Sources:
    """ Sources class to define the news source objects 
    """

    def __init__(self,name,author,content):
        self.name = name
        self.author = author
        self.content = content
