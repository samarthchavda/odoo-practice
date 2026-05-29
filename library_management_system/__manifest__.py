{
    'name': "Library Management System(main)",
    'description': "Library Management System",
    'depends':['base'],
    'data': [
        'views/sequence.xml',
        'views/Library_book_view.xml',
        'views/Library_member_view.xml',
        'views/book_issue_view.xml',
        'views/book_author_view.xml',
    ],
    'installable':True,
    'application':True,
}