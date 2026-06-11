from odoo import models,fields,api
from odoo.exceptions import ValidationError


class Studentmaster(models.Model):
    _name = 'stud.master.new'

    name = fields.Char("Name")
    phone_no = fields.Char("Phone")
    birth_date = fields.Date("Birth Date")
    active_student = fields.Boolean("Active Student",default=True)
    nationality = fields.Selection([('indian','Indian'),('non_indian','Non Indian')],string='Nationality')
    result_ids = fields.One2many('stud.result.new','student_id',string="Results")
    sp_act_ids = fields.Many2many('sports.act','stud_activities_rel','student_id','sports_id',string="Activities")

class StudResult(models.Model):
    _name = 'stud.result.new'
    _rec_name = "sr_no"
    
    sr_no = fields.Char("SR No")
    sub_1 = fields.Float("Sub 1")
    sub_2 = fields.Float("Sub 2")
    sub_3 = fields.Float("Sub 3")
    student_id = fields.Many2one('stud.master.new',string='Student')
    total_marks = fields.Float("Total Marks",compute='get_result',search='_search_total')
    percentage = fields.Float("Percent",compute='get_result',search='_search_total')

    def _search_total(self,operator,value):
        rec = self.search([]).filtered(
            lambda r : r.total_marks > value
        )
        return [('id','in',rec.ids)]

    def get_result(self):
        for rec in self:
            rec.total_marks = rec.sub_1 + rec.sub_2 + rec.sub_3
            rec.percentage = (rec.total_marks/3)

    # @api.onchange('sub_1','sub_2','sub_3')
    # def _onchange_total(self):
    #     self.total_marks = (self.sub_1 + self.sub_2 + self.sub_3)
    #     self.percentage = (self.total_marks / 3)

    # def calculate_result(self):
    #     self.total_marks = self.sub_1 + self.sub_2 + self.sub_3
    #     self.percentage = (self.total_marks/3)



class SportsActivities(models.Model):
    _name = 'sports.act'
    
    name = fields.Char("Title")
    stud_ids = fields.Many2many('stud.master.new','stud_activities_rel','sports_id','student_id',string="Students")
    