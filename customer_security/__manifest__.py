# -*- coding: utf-8 -*-
{
    'name': "Sale Person Related Contacts",
    'version': "13.0.1.0.0",
    'summary': """This Module is designed to see only Sale Person related Contacts""",
    'sequence': -100,
    'description': """This Module is design for sal person related contacts""",
    'category': 'Contacts',
    'author': "sadnan khan",
    'website': "http://www.softtar.com",
    'price': 9.99,
    'currency': 'EUR',
    'depends': ['base', 'contacts', 'sale', 'stock'],
    'data': [
        'security/customer_person.xml',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.own_documents.xml',
    ],
}
