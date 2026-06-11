from odoo import api,fields,models

class Course(models.Model):
    _name = 'training.course'
    _description = 'Training Course Model'

    name = fields.Char(string='Course Name')
    fees = fields.Float(string='Course Fees')
    duration_days = fields.Integer(string='Course Duration Days')
    is_active = fields.Boolean(string='Is Active')
    level = fields.Selection([
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced'),
    ],default='beginner',string='Course Level')

    batch_ids = fields.One2many(
        'training.batch',
        'course_id'
    )

    student_ids = fields.Many2many(
        'training.student'
    )