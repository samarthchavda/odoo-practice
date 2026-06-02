from odoo import fields, models
from odoo.exceptions import ValidationError

class Withdraw(models.Model):
    _name = 'bank.withdraw'
    _description = 'Withdraw'

    account_id = fields.Many2one(
        'bank.account.details',
        string='Account Number',
    )
    date = fields.Datetime(string='Date',default=fields.Date.today,readonly=True)
    withdraw_amount = fields.Float("Withdraw Amount", required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Withdrawn'),
    ], default='draft')

    def action_withdraw(self):
        for rec in self:

            if rec.status == 'done':
                raise ValidationError("Transaction already completed")

            if rec.withdraw_amount <= 0:
                raise ValidationError(
                    "Withdraw amount must be greater than zero"
                )

            if rec.account_id.balance < rec.withdraw_amount:
                raise ValidationError("Insufficient balance")

            rec.account_id.balance -= rec.withdraw_amount
            rec.status = 'done'

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Amount withdrawn successfully',
                'type': 'success',
                'sticky': False,
            }
        }


