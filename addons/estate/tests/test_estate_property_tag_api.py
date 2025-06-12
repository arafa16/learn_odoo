import json
import random

import requests
from odoo.tests import HttpCase


class TestEstatePropertyTagAPI(HttpCase):
	def setUp(self):
		super(TestEstatePropertyTagAPI, self).setUp()
		self.base_url = "http://localhost:8069"
		self.auth_token = "9224e47f-1bbc-45d0-a5cc-ca5dc7b25092"  # Replace with your actual auth token
		self.session_id = self.authenticate()

	def authenticate(self):
		url = f'{self.base_url}/web/session/authenticate'
		headers = {'Content-Type': 'application/json'}
		data = {
			"jsonrpc": "2.0",
			"method": "call",
			"id": 1,
			"method": "login",            
			"params": {
				"db": "db_odoo",
				"login": "admin@gmail.com",
				"password": "admin"
			},
		}

		response = requests.post(url, headers=headers, data=json.dumps(data))

	def test_get_tags(self):
		url = f'{self.base_url}/estate-property-tags'
		headers = {
			'Authorization': self.auth_token,
			'Cookie': f'session_id={self.session_id}'
		}
		response = requests.get(url, headers=headers)
		self.assertEqual(response.status_code, 200)
		
	def test_get_tag_by_id(self):
		tag_id = 1  # Replace with a valid tag ID
		url = f'{self.base_url}/estate-property-tag/{tag_id}'
		headers = {
			'Authorization': self.auth_token,
			'Cookie': f'session_id={self.session_id}'
		}
		
		response = requests.get(url, headers=headers)
		self.assertEqual(response.status_code, 200)
		
		expected_data = {
			'id': 1,
			'name': 'TAG 001',  # Replace with expected name
			'color': 11  # Replace with expected color
		}
		
		self.assertEqual(response.json(), expected_data)
		
	def test_create_tag(self):
		url = f'{self.base_url}/estate-property-tag'
		headers = {
			'Authorization': self.auth_token,
			'Cookie': f'session_id={self.session_id}',
			'Content-Type': 'application/json'
		}
		random_number = random.random()
		data = {
			"name": f"test{random_number}",
			"color": 99
		}

		response = requests.post(url, headers=headers, data=json.dumps(data))
		self.assertEqual(response.status_code, 201)
		
	def test_update_tag(self):
		updated_id = 1
		url = f'{self.base_url}/estate-property-tag/{updated_id}'
		headers = {
			'Authorization': self.auth_token,
			'Cookie': f'session_id={self.session_id}'
		}

		data = {
			"name": "TAG 001",
			"color": 11
		}

		response = requests.put(url, headers=headers, data=json.dumps(data))
		self.assertEqual(response.status_code, 201)

		expected_response = {
			"id": updated_id,
			"name": "TAG 001",
			"color": 11
		}
		self.assertEqual(response.json(), expected_response)
		
	def test_delete_tag(self):
		delete_id = 3
		url = f'{self.base_url}/estate-property-tag/{delete_id}'
		headers = {
			'Authorization': self.auth_token,
			'Cookie': f'session_id={self.session_id}'
		}

		response = requests.delete(url, headers=headers)
		self.assertEqual(response.status_code, 200)

		expected_response = {
			"id": delete_id,
			"message": f"Tag with id #{delete_id} has been deleted."
		}
		self.assertEqual(response.json(), expected_response)
		
	def test_unauthorized_request(self):
		url = f'{self.base_url}/estate-property-tags'
		response = requests.get(url)
		self.assertEqual(response.status_code, 401)
		self.assertIn('Un-authorized', response.text)