from copy import copy
from dateutil.relativedelta import relativedelta
from datetime import datetime
from email.policy import default
from sqlite3 import Date
import string
from odoo import api,fields,models

class PropertyOffer(models.Model):
    _name = "estate.property.offer"


    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date+relativedelta(days=(record.validity))
            else:
                record.date_deadline = datetime.now()+relativedelta(days=(record.validity))

    def _compute_inverse_deadline(self):
        for record in self:
            record.validity = record.date_deadline-record.create_date

    price = fields.Float()
    status = fields.Selection(selection=[("accepted","accepted"),("refused","Refused")],copy=False)
    partner_id = fields.Many2one ('res.partner', required=True)
    validity = fields.Integer(string="Validity (Days)",default=7)
    date_deadline = fields.Date(string="Deadline",compute="_compute_deadline", inverse="_compute_inverse_deadline")
    property_id = fields.Many2one ('estate.properties', required=True)

            
    
            