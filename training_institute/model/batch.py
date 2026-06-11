from odoo import api,models,fields

class Batch(models.Model):
    _name='training.batch'
    _description='Training Batch'

    name=fields.Char(string='Name')

    course_id=fields.Many2one(
        'training.course',
        string='Course',
    )
    start_date=fields.Date(string='Start Date',default=fields.Date.today())
    end_date=fields.Date(string='End Date')
    capacity=fields.Integer(string='Capacity')

    student_ids = fields.One2many(
        'training.student',
        'batch_id'
    )