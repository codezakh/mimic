import unittest
import re

import data_pipeline



class CommentPreprocessingTestCase(unittest.TestCase):
    def test_url_inserts_are_replaced(self):
        string_with_url_insert = """
        This is string with a url insert.[Url](http://website.com)The URL
        should be removed and replaced with URL_REPLACED.[another url](swag.com)
        """
        processed_string = re.sub(
            data_pipeline.match_url,
            'URL_REPLACED', 
            string_with_url_insert)
        print(processed_string)

if __name__ == '__main__':
    unittest.main()

