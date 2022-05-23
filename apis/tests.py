import json
import unittest

from app import create_app


class ApiTest(unittest.TestCase):
    endpoint = '/api/rules'
    content_type = 'application/json'

    def setUp(self) -> None:
        self.app = create_app().test_client()

    def test_find_all_success(self):
        response = self.app.get(self.endpoint)
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual(list, type(data))

    def test_add_success1(self):
        request = {
            'domain': 'www.o-r.cc',
            'owner': 'www.o-r.cc',
            'forwarding_protocol': 'https',
            'forwarding_domain': 'subshorts.com',
            'forwarding_code': 302,
            'forwarding_path': True,
        }
        response = self.app.post(self.endpoint, data=json.dumps(request), content_type=self.content_type)
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual('www.o-r.cc', data['domain'])
        self.assertEqual('www.o-r.cc', data['owner'])
        self.assertEqual('https', data['forwarding_protocol'])
        self.assertEqual('subshorts.com', data['forwarding_domain'])
        self.assertEqual(302, data['forwarding_code'])
        self.assertTrue(data['forwarding_path'])

    def test_add_success2(self):
        request = {
            'domain': 'www.iuy.me',
            'owner': 'www.iuy.me',
            'parking_title': 'Hello',
            'parking_content': 'world',
        }
        response = self.app.post(self.endpoint, data=json.dumps(request), content_type=self.content_type)
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual('www.iuy.me', data['domain'])
        self.assertEqual('www.iuy.me', data['owner'])
        self.assertEqual('Hello', data['parking_title'])
        self.assertEqual('world', data['parking_content'])

    def test_find_by_id_success(self):
        response = self.app.get(f'{self.endpoint}/1')
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, data['id'])


if __name__ == '__main__':
    unittest.main()
