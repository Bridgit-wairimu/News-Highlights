import unittest
from app.models import News
# News = news.News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news= News('Ex Radio Presenter: We suffered after Rose Kamotho sold Kameme fm' ,'Nairobi Traders in fear over planned evictions','11/28/2020','https://www.kenyans.co.ke/news/index.html','https://www.kenyans.co.ke/files/styles/article_300x150/public/images/media/Former%20radio%20presenter%20Karungo%20Thang%27wa.jpg?itok=5sDQy_rg','https://www.kenyans.co.ke/files/styles/article_style/public/images/media/Traders%20pictured%20in%20Gikomba%20Market%2C%20Nairobi..webp?itok=9_mWS-b-')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()
