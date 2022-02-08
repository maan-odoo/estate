from odoo import api,fields,models
from odoo.exceptions import UserError

class EstatePropert(models.Model):
    _name = "estate.properties"
    _description = "This is state core model"
    _order = "id desc"



    name = fields.Char(default="Unknow",required=True,string="Title")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    date_avalibility = fields.Date(string="Avaliable From",copy=False,default=lambda self: fields.Datetime.now())
    excepted_price = fields.Float(required=True,string="Excepected price")
    selling_price = fields.Float(string="Selling Price",readonly=True,copy=False)
    bedrooms = fields.Integer(string="Bedrooms",default="2")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area(sqm)")
    garden_orientation = fields.Selection(string="Garden Orientation",
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    state = fields.Selection(default="new",
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accept', 'Offer Accepted'), ('sold', 'Sold'), ('cancel', 'Canceled')])
    active = fields.Boolean(default="True")
    best_price = fields.Float(compute="_compute_best_price")
    total_area = fields.Float(compute="_compute_total_area")

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id")

    _sql_constraints = [
        ('ceck_excepted_price', 'check(excepted_price > 0)', "Excepted price must be Positive."),
        ('ceck_selling_price', 'check(selling_price > 0)', "Selling price must be Positive.")
    ]
    
    

    @api.depends("living_area","garden_area")
    def  _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area+record.garden_area
  

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            x = 0
            for offer in record.offer_ids:
                if offer.price > x:
                    x = offer.price
            record.best_price = x
    
    def unlink(self):
        for record in self:
            if record.state in ("new","cancel"):
                raise UserError("You can't Delete new or calcelled Properties")
        super(EstatePropert,self).unlink()
        
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = None

    def sold_property(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("Canceled properties cannot be sold.")
            record.state = "sold"
        return True

    def cancel_property(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold properties cannot be canceled.")
            record.state = "cancel"
        return True
        