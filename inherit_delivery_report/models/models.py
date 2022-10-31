# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class inherit_picking_report(models.Model):
#     _name = 'inherit_picking_report.inherit_picking_report'
#     _description = 'inherit_picking_report.inherit_picking_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
