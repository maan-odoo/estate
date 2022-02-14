from odoo import http 
from odoo.http import request


class RealEstate(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World! Welcome Real estate Site"

    @http.route('/hello_user', auth="user")
    def hello_usr(self, **kw):
        return "Hello %s" %(request.env.user.name)