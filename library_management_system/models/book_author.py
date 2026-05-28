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