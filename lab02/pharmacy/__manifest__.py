# -*- coding: utf-8 -*-
{
    'name': "pharmacy",

    'summary': """
        ITI pharmacy""",

    'description': """
        ITI pharmacy
    """,

    'author': "My Company",
    'website': "https://www.iti.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/doctors.xml',
        'views/medicine.xml',
        'views/sales.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
