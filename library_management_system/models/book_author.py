from odoo import api, fields, models

class BookAuthor(models.Model):
    _name = "book.author"
    _description = "Book Author"

    name = fields.Char(required=True)
    book_ids = fields.One2many(
        'library.book',
        'author_id',
        string="Book",
    )
    book_count = fields.Integer("Book", compute='_compute_book_count')

    # def _compute_book_count(self):
    #     for rec in self:
    #         rec.book_count = rec.env['library.book'].search_count([
    #             ('author_id', '=', rec.id)
    #         ])
    #
    # def action_view_book(self):
    #     books = self.env['library.book'].search([
    #         ('author_id', '=', self.id)
    #     ])
    #     return {
    #          'type': 'ir.actions.act_window',
    #         'name': 'Book ',
    #         'res_model': 'library.book',
    #         'view_mode': 'list,form',
    #         'domain': [('id','in',books.ids)],
    #         }
