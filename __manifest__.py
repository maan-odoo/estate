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
        "views/property_type_view.xml",
        "views/property_tag_view.xml",
        "views/property_offer_view.xml",
        "views/estate_menus.xml",
        "wizard/asign_buyer_view.xml",
        "security/ir.model.access.csv"
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}