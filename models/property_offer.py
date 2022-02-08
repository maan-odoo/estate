
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from odoo.exceptions import UserError
from odoo import api,fields,models

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description ="This is manage the offer of property"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(selection=[("accepted","accepted"),("refused","Refused")],copy=False)
    partner_id = fields.Many2one ('res.partner', required=True)
    validity = fields.Integer(string="Validity (Days)",default=7)
    date_deadline = fields.Date(string="Deadline",compute="_compute_deadline", inverse="_compute_inverse_deadline")
    property_id = fields.Many2one ('estate.properties', required=True)

    _sql_constraints = [
        ('ceck_excepted_price', 'check(excepted_price > 0)', "Excepted price must be Positive.")]

    @api.constrains("price")
    def _check_price(self):
        for record in self:
            x = record.property_id.excepted_price
            c = (x*90)/100
            if not record.price>=c:
                raise UserError("The offer must be 90% of excepted Price")

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
                diff = datetime.strptime(record.date_deadline.strftime('%Y-%m-%d'), '%Y-%m-%d') - record.create_date
                record.validity = diff.days + 1
            else:
                record.validity = (datetime.strptime(record.date_deadline.strftime('%Y-%m-%d'), '%Y-%m-%d') - datetime.today())+1
            
    def action_accept(self):
        for record in self:
            if record.status == 'refused':
                raise UserError("Refused offer cannot be accepted.")
            record.status = "accepted"
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
        return True

    def action_refuse(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError("Accepted offer cannot be refused.")
            record.status = "refused"
        return True
            
    
            