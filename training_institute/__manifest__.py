{
    'name':'training_institute',
    'description':"training institute management",
    'depends':['base'],
    'data':[
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/course.xml',
        'views/batch.xml',
        'views/student.xml',
        'views/menu.xml',
    ],
    'application':True,
    'installable':True,
}