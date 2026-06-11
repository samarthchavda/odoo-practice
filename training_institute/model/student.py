from odoo import fields,models,api

class Student(models.Model):
    _name = 'training.student'
    _description = 'Student'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ],string='Gender')

    course_ids = fields.Many2many(
        'training.course',
        string='Courses',
    )

    batch_id = fields.Many2one(
        'training.batch',
        string='Batch',
    )
