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

    from odoo import fields

    def action_pay(self):
        for rec in self:
            rec.status = 'paid'

            rec.env['loan.history'].create({
                'loan_id': rec.loan_id.id,
                'customer_id': rec.loan_id.customer_id.id,
                'loan_number': rec.loan_id.loan_number,
                'installment_date': rec.installment_date,
                'amount': rec.amount,
            })