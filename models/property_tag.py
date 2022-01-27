from odoo import models, fields

class PropertyTag(models.Model):
    _name = 'estate.property.tag'

    name = fields.Char(required=True)