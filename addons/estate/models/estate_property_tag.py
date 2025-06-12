from odoo import fields, models, api
from odoo.exceptions import ValidationError


class EstatePropertyTag(models.Model):

    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")

    @api.constrains("color")
    def _check_color(self):
        for tag in self:
            if tag.color > 100:
                raise ValidationError("Color index must be less than or equal to 100.")
