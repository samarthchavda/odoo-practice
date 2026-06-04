from dateutil.relativedelta import relativedelta
from odoo import api,fields,models
from odoo.exceptions import ValidationError


class LoanApplication(models.Model):
    _name = 'loan.application'
    _description = 'Loan Application'

    loan_number = fields.Char(string='Loan Number',required=True,readonly=True,copy=False,default='loan')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('loan_number') or vals.get('loan_number') == 'loan':
                vals['loan_number'] = self.env['ir.sequence'].next_by_code('loan.application.sequence')

        return super().create(vals_list)

    customer_id = fields.Many2one(
        'bank.customer',
        string='Customer',
    )
    status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    ],default='draft',readonly=True)

    loan_amount = fields.Float(
        string='Loan Amount',
        required=True
    )

    interest_rate = fields.Float(
        string='Interest Rate (%)',
        required=True
    )

    duration = fields.Integer(
        string='Duration (Years)',
        required=True
    )

    monthly_emi = fields.Float(
        string='Monthly EMI',
        compute='_get_monthly_emi',
        store=True,
        readonly=True
    )

    installment_ids = fields.One2many(
        'loan.installment',
        'loan_id',
        string='Installments'
    )

    def action_approved(self):
        pass

    def action_reject(self):
        pass

    def action_close(self):
        pass

    def action_pay_all(self):
        pass
