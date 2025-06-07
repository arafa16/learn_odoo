from odoo import http
import json
import requests

class EstateProperty(http.Controller):
	@http.route('/healthcheck', auth='public', methods=['GET', 'POST'])
	def healthcheck(self, **kw):
		return "IT Works"

	@http.route('/xyz', auth='user')
	def xyz(self, **kw):
		return "This is accessible for authenticated user"

	@http.route('/entries', auth='public')
	def entries(self, **kw):
		response = requests.get("https://freedictionaryapi.com/api/v1/entries/en/public")
		return json.dumps(response.json())