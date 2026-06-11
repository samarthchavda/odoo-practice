from odoo import models,fields,api

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    blood_group = fields.Char(string='Blood Group')
    appointment_ids = fields.One2many(
        'hospital.appointment',
        'patient_id',
        string='Appointments',
    )