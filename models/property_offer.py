from copy import copy
from dateutil.relativedelta import relativedelta
from datetime import datetime

from odoo import api,fields,models

class PropertyOffer(models.Model):
    _name = "estate.property.offer"

    price = fields.Float()
    status = fields.Selection(selection=[("accepted","accepted"),("refused","Refused")],copy=False)
    partner_id = fields.Many2one ('res.partner', required=True)
    validity = fields.Integer(string="Validity (Days)",default=7)
    date_deadline = fields.Date(string="Deadline",compute="_compute_deadline", inverse="_compute_inverse_deadline")
    property_id = fields.Many2one ('estate.properties', required=True)

    @api.depends("validity", "create_date")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date+relativedelta(days=(record.validity))
            else:
                record.date_deadline = datetime.now()+relativedelta(days=(record.validity))

    def _compute_inverse_deadline(self):
        for record in self:
            if record.create_date:
                # record.validity = int(record.date_deadline-record.create_date)
                import pdb
                pdb.set_trace()
                diff = datetime.strptime(record.date_deadline.strftime('%Y-%m-%d'), '%Y-%m-%d') - record.create_date
                record.validity = diff.days
            else:
                # record.validity = int(record.date_deadline-datetime.now())
                record.validity = 4
            
            # record.validity = record.date_deadline-record.create_date
            # record.validity = datetime.now()

            
    
            