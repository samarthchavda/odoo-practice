from odoo import models, fields

class LoanInstallment(models.Model):
    _name = 'loan.installment'
    _description = 'Loan Installment'

    loan_id = fields.Many2one(
        'loan.application',
        string='Loan',
        required=True
    )

    amount = fields.Float(
        related='loan_id.monthly_emi',
        string='EMI Amount',
        store=True,
        readonly=True,
    )

    installment_date = fields.Date(
        string='Installment Date',
        required=True,
        default=fields.Date.today(),
        readonly=True,
    )

    status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ], default='unpaid',readonly=True)

    def action_pay(self):
        self.status = 'paid'