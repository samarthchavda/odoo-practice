# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Student Management New',
    'summary': 'Manage students',
    'description':'Manage students',   
    'depends': ['base'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        ],
    'installable': True,
}
