from odoo import fields, models, api

class library_member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    # _rec_name = 'user_id'

    user_id = fields.Many2one('res.users')
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    is_active = fields.Boolean(default=True)

    issue_book_ids = fields.One2many(
        'book.issue',
        'member_id',
        string='Issues',
    )