from odoo import fields,models
from odoo.exceptions import ValidationError

class BankDeposit(models.Model):
    _name = 'bank.deposit'
    _description = 'Bank Deposit'

    account_id = fields.Many2one(
        'bank.account.details',
        string="Account NO",
    )
    date = fields.Datetime(string="Date",default=fields.Date.today,readonly=True)
    deposit_amount = fields.Float(string="Amount",required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Deposited')
    ], default='draft')

    def action_deposit(self):
        for rec in self:
            if rec.deposit_amount < 0 :
                raise ValidationError("Deposit amount cannot be negative")

            rec.account_id.balance += rec.deposit_amount
            rec.status = 'done'

            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Success',
                    'message': 'Amount deposited successfully',
                    'type': 'success',
                }
            }
