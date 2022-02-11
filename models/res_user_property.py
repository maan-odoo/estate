from odoo import _,api,fields,models

class ResUserProperties(models.Model):
    _name = "res.users"
    _inherit = "res.users"

    property_ids = fields.One2many("estate.properties","salesperson_id")
