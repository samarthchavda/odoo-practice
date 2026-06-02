from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import readonly


class BankTransaction(models.Model):
    _name = 'bank.transaction'
    _description = 'Bank Transaction'

    transaction_number = fields.Char(
        string="Transaction Number",
        readonly=True,
        copy=False,
        default='New',
    )
    from_account_id = fields.Many2one(
        'bank.account.details',
        string='Sender Account',
        required=True
    )
    to_account_id = fields.Many2one(
        'bank.account.details',
        string='Receiver Account',
        required=True
    )
    amount = fields.Float(
        string='Amount',
        required=True
    )
    date = fields.Date(
        string='Transaction Date',
        default=fields.Date.today,
        readonly=True
    )
    remarks = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done')
    ], default='draft')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('transaction_number', 'New') == 'New':
                vals['transaction_number'] = self.env['ir.sequence'].next_by_code(
                    'bank.transaction.sequence'
                ) or 'New'

        return super().create(vals_list)

    def action_transfer(self):
        for rec in self:
            if rec.from_account_id == rec.to_account_id:
                raise ValidationError(
                    "Sender and receiver account cannot be same"
                )
            if rec.amount <= 0:
                raise ValidationError(
                    "amount must be greater than zero"
                )
            if rec.from_account_id.balance < rec.amount:
                raise ValidationError(
                    "insufficient balance"
                )
            rec.from_account_id.balance -= rec.amount
            rec.to_account_id.balance += rec.amount
            rec.state = 'done'