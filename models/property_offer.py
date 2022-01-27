from copy import copy
from odoo import fields,models

class PropertyOffer(models.Model):
    _name = "estate.property.offer"

    price = fields.Float()
    status = fields.Selection(selection=[("accepted","accepted"),("refused","Refused")],copy=False)
    partner_id = fields.Many2one ('res.partner', required=True)
    property_id = fields.Many2one ('estate.properties', required=True)
