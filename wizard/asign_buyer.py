from odoo import _, api, fields, models

class AsignBuyer(models.TransientModel):
    _name = "asign.buyer"

    buyer_id = fields.Many2one("res.partner", string="Buyer")

    def action_asign_buyer(self):
        self.ensure_one()
        Session = self.env['estate.properties']
        ids = self.env.context.get('active_ids')
        sessions = Session.browse(ids)
        sessions.write({'buyer_id': self.buyer_id})
        return True