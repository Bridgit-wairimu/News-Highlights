class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,name,title,description,publishedAt,content,url,urlToImage):
        self.name = name
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage