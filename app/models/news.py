class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,description,publishedAt,content,url,urlToImage):
        self.id = id
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage