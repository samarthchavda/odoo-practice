from odoo import models

class LoanXlsxReport(models.AbstractModel):
    _name = 'report.loan.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self,workbook,data,loans):

        sheet = workbook.add_worksheet('loans')

        sheet.write(0,0,'Loan Number')
        sheet.write(0, 1, 'Customer')
        sheet.write(0, 2, 'Amount')
        sheet.write(0, 3, 'EMI')
        sheet.write(0, 4, 'Status')

        row = 1

        for loan in loans:
            sheet.write(row, 0, loan.loan_number)
            sheet.write(row, 1, loan.customer_id.name or '')
            sheet.write(row, 2, loan.loan_amount)
            sheet.write(row, 3, loan.monthly_emi)
            sheet.write(row, 4, loan.status)

            row += 1