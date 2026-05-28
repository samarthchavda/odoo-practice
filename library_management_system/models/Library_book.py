from odoo import fields,models,api
from odoo.exceptions import ValidationError

class Library_Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    book_number = fields.Char(string="Book Id", required=True, copy=False, default="book",readonly=True)
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('book_number') or vals.get('book_number') == "book":
                vals['book_number'] = self.env['ir.sequence'].next_by_code('library.book.number') or 'book'

        return super().create(vals_list)


    name = fields.Char(string='Name')
    author = fields.Char(string='Author')
    available_qty = fields.Integer(string='Available Qty')
    is_available = fields.Boolean(compute='_compute_is_available',store=True)

    @api.constrains('available_qty')
    def _available_qty_check(self):
        if self.available_qty < 0:
            raise ValidationError("Available Qty is not negative")

    @api.depends('available_qty')
    def _compute_is_available(self):
            self.is_available = self.available_qty > 0



