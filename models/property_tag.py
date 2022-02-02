from odoo import models, fields

class PropertyTag(models.Model):
    _name = 'estate.property.tag'

    name = fields.Char(required=True)
    _sql_constraints = [
        ('tag_value_name', 'unique(name)', "Property Tag should be unique.")
    ]