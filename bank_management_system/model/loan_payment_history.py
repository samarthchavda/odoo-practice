from odoo import models, fields,api

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

    installment_no = fields.Char(
        string='Installment No',
        required=True,
        readonly=True,
        copy=False,
        default='New'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('installment_no') or vals.get('installment_no') == 'New':
                vals['installment_no'] =self.env['ir.sequence'].next_by_code('loan.history.sequence')

        return super().create(vals_list)

    payment_date = fields.Date(
        string='Payment Date',
        default=fields.Date.today
    )

    amount = fields.Float(
        string='Amount Paid'
    )
