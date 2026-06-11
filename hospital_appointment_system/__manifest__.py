{
    'name': 'hospital_appointment_system',
    'description': 'hospital Appointment System',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/patient.xml',
        'views/menu.xml',
    ],
    'application': True,
    'installable': True,
}