import unittest
from app.models import Sources
# Sources = sources.Sources

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('The Star Online','Dr Helmy Haja Mydin','Blockchain technology has featured prominently in the public imagination since the invention of Bitcoin by an unknown person or group of people going by the name Satoshi Nakamoto in 2008.\r\nIn fact, t… [+7207 chars]'
    
    # def test_init(self):
    #     self.assertEqual(self.new_source.name,"The Star Online")
    #     self.assertEqual(self.new_source.author,"Dr Helmy Haja Mydin")
    #     self.assertEqual(self.new_source.content,"Blockchain technology has featured prominently in the public imagination since the invention of Bitcoin by an unknown person or group of people going by the name Satoshi Nakamoto in 2008.\r\nIn fact, t… [+7207 chars]")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
        



if __name__ == '__main__':
    unittest.main()