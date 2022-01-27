# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real estate',
    'version': '1.3',
    'category': 'RealEstate',
    'sequence': 15,
    'summary': 'Manage Real Estate Sevices',
    'description': "",
    'website': 'https://www.odoo.com',
    'depends': [],
    'data': [
        "views/property_view.xml",
        "views/estate_menus.xml",
        "views/property_type_view.xml",
        "views/property_tag_view.xml",
        "views/property_offer_view.xml",
        "security/ir.model.access.csv"
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}