from odoo import models, fields

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate property type'

    name = fields.Char(required=True)
    _sql_constraints = [
        ('type_unique', 'unique(name)', "Property Type should be unique.")
    ]