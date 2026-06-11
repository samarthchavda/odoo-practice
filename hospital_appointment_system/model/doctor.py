from odoo import api, fields, models

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'

    name = fields.Char("Doctor Name")
    specialization = fields.Char("specialization")
    experience_years = fields.Char("experience_years")
    is_available = fields.Boolean("Available")
    appointment_ids = fields.One2many(
        'hospital.appointment',
        'doctor_id',
        string='Appointments',
    )