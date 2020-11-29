class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,publishedAt,content,url,urlToImage):
        self.author= author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage