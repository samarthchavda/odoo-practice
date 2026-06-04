from odoo import api,fields,models

class Bank_account_details(models.Model):
    _name = 'bank.account.details'
    _description = 'Bank Account Details'
    _rec_name = 'customer_id'

    customer_id = fields.Many2one(
        'bank.customer',
        string='Account Holder',
    )
    account_number = fields.Char("Account Number",required=True,readonly=True,copy=False,default='ACC')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('account_number') or vals.get('account_number') == 'ACC':
                vals['account_number'] = self.env['ir.sequence'].next_by_code('bank.account.sequence') or 'ACC'

        return super().create(vals_list)

    account_type = fields.Selection([
        ('saving','Saving'),
        ('business','Business'),
    ])
    balance = fields.Float("Balance")

    transaction_ids = fields.One2many(
        'bank.transaction',
        'from_account_id',
        string='Transactions',
    )
    deposit_ids = fields.One2many(
        'bank.deposit',
        'account_id',
        string='Deposits',
    )
    withdraw_ids = fields.One2many(
        'bank.withdraw',
        'account_id',
        string='Withdraws',
    )
