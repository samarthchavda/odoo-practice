from odoo import fields, models, api

class Project(models.Model):
    _name = 'my.project'
    _description = 'Project Management'

    name = fields.Char(string='Name')
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer'
    )
    budget = fields.Integer(string='Budget')
    is_active = fields.Boolean(string='Is Active')
    task_ids = fields.One2many(
        'my.task',
        'project_id',
        string='Tasks',
    )