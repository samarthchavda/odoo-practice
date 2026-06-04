from odoo import fields, models, api

class CustomerDetails(models.Model):
    _name = 'bank.customer'
    _description = 'Customer Details'

    name = fields.Char(string="Customer Name",required=True)
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email Address")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    aadhar_card_number = fields.Char(string="Aadhar Card Number")
    pancard_number = fields.Char(string="Pancard Number")
