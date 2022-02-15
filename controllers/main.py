from urllib import response
from odoo  import http 
from odoo.http import request


class RealEstate(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World! Welcome Real estate Site"

    @http.route('/hello_user', auth="user")
    def hello_usr(self, **kw):
        return "Hello %s" %(request.env.user.name)

    @http.route('/first',auth="public")
    def first_temp(self,**kw):
        return request.render('estate.first_template')

    @http.route('/property',auth="user",website="True")
    def showProperty(self,**kw):
        return request.render("estate.property_template",{})

        
