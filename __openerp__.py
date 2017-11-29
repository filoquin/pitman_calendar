# -*- coding: utf-8 -*-
{
    'name': "pitman calendar",

    'summary': """
        Calendar""",

    'description': """
        Academy calendar
    """,

    'author': "Hormiga G",
    'website': "Hormiga G",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['pitman_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pit_calendar.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}