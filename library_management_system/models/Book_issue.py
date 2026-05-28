from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Book_issue(models.Model):
    _name = 'book.issue'
    _description = 'Book Issue'

    book_id = fields.Many2one(
        'library.book',
        string='Book',
    )

    member_id = fields.Many2one(
        'library.member',
        string='Member',
    )
    issue_date = fields.Date(string='Date of Issue',default=fields.Date.today(),required=True)
    return_date = fields.Date(string='Date of Return')
    day_issue = fields.Integer(string='issue Days', compute='_compute_day_issue')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('issue', 'Issue'),
        ('return', 'Return'),
    ],default='draft')

    @api.depends('issue_date','return_date')
    def _compute_day_issue(self):
        for book in self:
            if book.issue_date and book.return_date:
                book.day_issue = (book.return_date - book.issue_date).days
            else:
                book.day_issue = 0

    # @api.onchange('issue_date')
    # def _onchange_issue_book(self):
    #     if self.issue_date:
    #         self.status = 'issue'

    @api.constrains('issue_date')
    def _check_issue_book(self):
        if self.issue_date:
            self.status = 'issue'

    @api.constrains('return_date')
    def _check_return_book(self):
        if self.return_date:
            self.status = 'return'
        if self.day_issue < 0:
            raise ValidationError("value cannot be negative please select proper date")

    # @api.onchange('issue_date','return_date')
    # def _onchange_issue_book_count(self):
    #     for book in self:
    #         if book.status == 'issue':
    #             book.book_id.available_qty -= 1
    #         if book.status == 'return':
    #             book.book_id.available_qty += 1

    # def action_issue_book(self):
    #     if self.status == 'issue':
    #         self.book_id.available_qty -= 1
    #
    # def action_return_book(self):
    #     if self.status == 'return':
    #         self.book_id.available_qty += 1

    # penalty logic
    # fine = late_days * 10
    # due_date = issue.date + timedelta(days=7).days
    # late_days = due_date * 10
    # timedlta added and substract to date or time
    # list []
    # set {}
    # tuples ()
    # dict = {key:value}

    # fine = fields.Integer(string='Fine',compute='_compute_fine_amount',store=True)
    # @api.depends('late_days')
    # def _compute_fine_amount(self):
    #     for rec in self:
    #         rec.fine = rec.late_days * 10
    #
    # due_date = fields.Date(string='Due Date',compute='_compute_due_date',store=True)
    # @api.depends('issue_date')
    # def _compute_due_date(self):
    #     for rec in self:
    #         rec.due_date = rec.issue_date + timedelta(days=7)
    #
    # late_days = fields.Integer(string='Late Days', compute='_compute_late_days',store=True)
    # @api.depends('due_date','return_date')
    # def _compute_late_days(self):
    #     for rec in self:
    #         if rec.return_date and rec.due_date:
    #             if rec.return_date > rec.due_date:
    #                 rec.late_days = (rec.return_date - rec.due_date).days

