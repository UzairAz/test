# -*- coding: utf-8 -*-
{
    'name': "Product Modification",
    'summary': """Add Extra Fields to Product template and Product Variants""",
    'description': """
        Add Extra Fields to Product template and Product Variants
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/type_segment_view.xml',
    ]
}
