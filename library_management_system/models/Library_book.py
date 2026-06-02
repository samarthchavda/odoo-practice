from itertools import repeat

from odoo import fields,models,api
from odoo.exceptions import ValidationError

class Library_Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    book_number = fields.Char(string="Book Number", required=True, copy=False,readonly=True,default='book')
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('book_number') or vals.get('book_number') == 'book':
                vals['book_number'] = self.env['ir.sequence'].next_by_code('library.book.sequence') or 'book'
        return super().create(vals_list)

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


    # when you don't know the deatils of record and you have to serach that time use and edit after that a search and
    # browse also use of same but there is you know of record id and that will search the that record
    # def book_update_name(self):
    #     book = self.env['library.book'].search([('book_number','=','B0001')], limit=1)
    #     book.write({'name': 'advance python book'})
    #

    #is use for the condition while you have to delete a record
    # def unlink(self):
    #     for rec in self:
    #         if rec.available_qty > 0:
    #             raise ValidationError("You cannot delete book")
    #
    #     return super().unlink()

    issue_ids = fields.One2many(
        'book.issue',
        'book_id',
        string='Issues',
    )