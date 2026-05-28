from odoo import fields, models, api

class library_member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    is_active = fields.Boolean(default=True)