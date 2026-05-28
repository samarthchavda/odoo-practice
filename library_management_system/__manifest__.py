{
    'name': "Library Management System(main)",
    'description': "Library Management System",
    'depends':['base'],
    'data': [
        'views/Library_book_view.xml',
        'views/Library_member_view.xml',
        'views/book_issue_view.xml',
        'views/sequence.xml',
    ],
    'installable':True,
    'application':True,
}