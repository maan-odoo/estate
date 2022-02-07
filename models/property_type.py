from email.policy import default
from odoo import models, fields

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate property type'
    _order = "name"

    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence',default=1)
    property_ids = fields.One2many("estate.properties","property_type_id")
    _sql_constraints = [
        ('type_unique', 'unique(name)', "Property Type should be unique.")
    ]