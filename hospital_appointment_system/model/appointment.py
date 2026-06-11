from odoo import fields, models


class appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'appointment'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
    )
    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Doctor',
    )
    appointment_date = fields.Datetime(string='Appointment Date',default=fields.Date.today())
    fees = fields.Integer(string='Fees')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ],default='draft',string='Status',readonly=True)
    is_paid = fields.Boolean(string='Is Paid',readonly=True)

    def action_pay_amount(self):
        for rec in self:
            if rec.fees > 0:
                rec.status = 'done'
                rec.is_paid = True