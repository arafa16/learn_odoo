from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError

class TestEstatePropertyTag(TransactionCase):

	def setUp(self):
		super(TestEstatePropertyTag, self).setUp()
		self.estate_property_tag_model = self.env['estate.property.tag']

	def test_create_tag(self):
		tag_data = {
			'name': 'TAG 001',
			'color': 99
		}
		tag = self.estate_property_tag_model.create(tag_data)
		self.assertEqual(tag.name, 'TAG 001')
		self.assertEqual(tag.color, 99)

	def test_read_tag(self):
		new_tag = self.estate_property_tag_model.create({
			'name': 'TAG 002',
			'color': 1
		})
		tag = new_tag.read(['name', 'color'])
		self.assertEqual(tag[0]['name'], 'TAG 002')
		self.assertEqual(tag[0]['color'], 1)

	def test_update_tag(self):
		tag = self.estate_property_tag_model.create({
			'name': 'TAG 003',
			'color': 2
		})

		tag.write({'color': 3})
		self.assertEqual(tag.color, 3)

	def test_update_with_invalid_color(self):
		with self.assertRaises(ValidationError) as context:
			tag = self.estate_property_tag_model.create({
				'name': 'TAG 004',
				'color': 79
			})
			tag.write({'color': 101})
		self.assertEqual(str(context.exception), "Color index must be less than or equal to 100.")

	def test_delete_tag(self):
		tag = self.estate_property_tag_model.create({
			'name': 'TAG 005',
			'color': 4
		})
		tag.unlink()
		check_tag = self.estate_property_tag_model.search([('name', '=', 'TAG 005')])
		self.assertFalse(check_tag, "Tag should be deleted, but it still exists.")
