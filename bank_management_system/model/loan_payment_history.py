from odoo import models, fields

class LoanPaymentHistory(models.Model):
    _name = 'loan.payment.history'
    _description = 'Loan Payment History'

    loan_id = fields.Many2one(
        'loan.application',
        string='Loan'
    )

    loan_installment_id = fields.Many2one(
        'loan.installment',
        string='Installment'
    )

    loan_number = fields.Char(
        related='loan_id.loan_number',
        store=True
    )

    amount = fields.Float(
        related='loan_installment_id.amount',
        store=True
    )

    installment_date = fields.Date(
        related='loan_installment_id.installment_date',
        store=True
    )

    status = fields.Selection(
        related='loan_installment_id.status',
        store=True
    )