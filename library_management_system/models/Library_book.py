from odoo import fields,models,api
from odoo.exceptions import ValidationError

class Library_Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    author_id = fields.Many2one('book.author', string="Author")
    name = fields.Char(string='Name')
    available_qty = fields.Integer(string='Available Qty')
    is_available = fields.Boolean(compute='_compute_is_available',store=True)

    @api.constrains('available_qty')
    def _available_qty_check(self):
        if self.available_qty < 0:
            raise ValidationError("Available Qty is not negative")

    @api.depends('available_qty')
    def _compute_is_available(self):
            self.is_available = self.available_qty > 0



