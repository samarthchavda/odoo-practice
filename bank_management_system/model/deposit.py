from odoo import fields,models,api

class BankDeposite(models.Model):
    _name = 'bank.deposite'
    _description = 'Bank Deposite'

    account_id = fields.Many2one(
        'bank.account.details',
        string="Account NO",
        compute='_compute_account_id',
    )
    date = fields.Datetime(string="Date",default=fields.Date.today)
    deposite_amount = fields.Float(string="Amount")

    @ap