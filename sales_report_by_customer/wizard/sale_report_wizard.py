# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class SaleReport(models.TransientModel):
    _name = 'sale.wizard'
    _description = 'Sales Report'

    date_from = fields.Date(string='Date From', required=True, default=datetime.today())
    date_to = fields.Date(string='Date To', required=True, default=datetime.today())
    partner_id = fields.Many2many('res.partner', string="Customer")
    user_ids = fields.Many2many('res.users', string="Sales Person")
    report_for = fields.Selection([('customer', 'Customer'), ('sale_person', 'Sales Person')], default='customer')

    @api.onchange('report_for')
    def _onchange_report_for(self):
        if self.report_for == 'customer':
            self.user_ids == None
        elif self.report_for == 'sale_person':
            self.partner_id = None
        else:
            self.partner_id = None

    @api.constrains('date_to', 'date_from')
    def date_constrains(self):
        for rec in self:
            if rec.date_to < rec.date_from:
                raise ValidationError(_('Sorry, End Date Must be greater Than Start Date...'))

    def print_pdf_action(self):
        data = {
            'model': 'sale.wizard',
            'ids': self.ids,
            'form': {
                'date_from': self.date_from, 'date_to': self.date_to, 'customer': self.partner_id,
                'report_for': self.report_for,
                'selected_id_list': self.partner_id.ids if self.partner_id else self.env['res.partner'].search([]).ids,
                'selected_user_id_list': self.user_ids.ids if self.user_ids else self.env['res.users'].search(
                    []).ids,
            },
        }
        # ref `module_name.report_id` as reference.
        return self.env.ref('sales_report_by_customer.sale_report_customer').report_action(self, data=data)


class InheritAccountPayment(models.Model):
    _inherit = 'account.payment'
