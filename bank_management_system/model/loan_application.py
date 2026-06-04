from dateutil.relativedelta import relativedelta
from odoo import api,fields,models
from odoo.exceptions import ValidationError


class LoanApplication(models.Model):
    _name = 'loan.application'
    _description = 'Loan Application'
    _rec_name = 'customer_id'

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
    @api.depends('duration','loan_amount')
    def _get_monthly_emi(self):
        for rec in self:
            month = rec.duration * 12
            if rec.loan_amount and rec.duration:
                rec.monthly_emi = rec.loan_amount / month

    def action_approved(self):
        self.status = 'approved'

    def action_reject(self):
        self.status = 'rejected'

    def action_close(self):
        self.status = 'closed'

    def action_pay_all(self):
        pass
