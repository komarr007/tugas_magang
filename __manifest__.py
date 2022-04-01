# -*- coding: utf-8 -*-
{
    'name': "inherit tugas 2",

    'summary': """kontol anjing""",

    'description': """
        bangsat kontol
    """,

    'author': "your another self",
    'website': "komarr007.github.io/RIGAQI",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['sale','base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_inherit_views.xml',
        # 'views/note_page_views.xml',
        # 'views/daily_checker_views.xml',
        # 'views/yt_video_download_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
