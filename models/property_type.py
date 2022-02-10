from email.policy import default

from matplotlib import offsetbox
from odoo import models, fields

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate property type'
    _order = "name"

    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence',default=1)
    property_ids = fields.One2many("estate.properties","property_type_id")
    offer_ids = fields.One2many("estate.property.offer","property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    _sql_constraints = [
        ('type_unique', 'unique(name)', "Property Type should be unique.")
    ]

    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids) 

    def action_offer_count_btn(self):
        pass
        
        