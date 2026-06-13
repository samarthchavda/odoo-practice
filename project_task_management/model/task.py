from odoo import models, fields

class Task(models.Model):
    _name = 'my.task'
    _description = 'My Task'

    name = fields.Char(string='Name')
    project_id = fields.Many2one(
        'my.project',
        string='Project'
    )
    assignee_to = fields.Many2one(
        'res.users',
        string='Assignee To',
    )
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ],default='medium',string='Priority')

    estimated_hours = fields.Float(string='Estimated Hours')

    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ],default='in_progress',string='Status',readonly=True)

    def action_complete_task(self):
        self.status = 'done'