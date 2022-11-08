# -*- coding: utf-8 -*-
{
    'name': "Sales By Customer Report",
    'summary': """ This Module is used to check sales by customers and sales person in a specific dates""",
    'description': """ This Module is used to check sales by customer and sales person in a specific date""",
    'author': "",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '15.0.0.1',
    'depends': ['base', 'account', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_report_wizard.xml',
        'reports/sale_report.xml',
        'reports/sale_customer_report_template.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
