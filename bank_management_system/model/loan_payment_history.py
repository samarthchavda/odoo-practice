from odoo import models, fields

class LoanHistory(models.Model):
    _name = 'loan.history'
    _description = 'Loan Payment History'
    _order = 'payment_date desc'

    loan_id = fields.Many2one(
        'loan.application',
        string='Loan',
        required=True
    )

    customer_id = fields.Many2one(
        'bank.customer',
        string='Customer',
        required=True
    )

    loan_number = fields.Char(
        string='Loan Number',
        required=True
    )

    installment_no = fields.Integer(
        string='Installment No'
    )

    installment_date = fields.Date(
        string='Installment Date'
    )

    payment_date = fields.Date(
        string='Payment Date',
        default=fields.Date.today
    )

    amount = fields.Float(
        string='Amount Paid'
    )
