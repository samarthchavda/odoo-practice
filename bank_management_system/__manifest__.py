{
    'name': 'Bank Management System',
    'description': "Bank Management System",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sequence.xml',
        'views/bank_account_details.xml',
        'views/customer_details.xml',
        'views/transaction.xml',
        'views/deposit.xml',
        'views/withdraw.xml',
    ],
    'application': True,
    'installable': True,
}
