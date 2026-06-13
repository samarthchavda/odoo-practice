{
    'name': 'project & task management',
    'description': 'Project & Task Management',
    'depends':['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/project.xml',
        'views/task.xml',
        'views/menu.xml',
    ],
    'application': True,
    'installable': True,
}