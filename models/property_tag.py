from odoo import models, fields

class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = "This is manage the tag of propertires"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer("Color")
    _sql_constraints = [
        ('tag_value_name', 'unique(name)', "Property Tag should be unique.")
    ]