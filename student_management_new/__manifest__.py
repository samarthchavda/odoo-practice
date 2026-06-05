{
    'name': 'Student Management New',
    'summary': 'Manage students',
    'description':'Manage students',   
    'depends': ['base'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'data/stud.master.new.csv',
        'views/views.xml',
        ],
    'installable': True,
}
