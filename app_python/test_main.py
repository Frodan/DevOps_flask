import unittest
import os

import main


class MyTestCase(unittest.TestCase):
    def test_env(self):
        self.assertIsNotNone(os.environ['USER_LOGIN'])
        self.assertIsNotNone(os.environ['USER_PASS'])
        print("ENV is OK")

    def setUp(self):
        self.app = main.app.test_client()

    def test_main_page(self):
        response = self.app.get('/get_wallet', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("Status 200, OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
