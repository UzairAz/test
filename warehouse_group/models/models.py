# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritStockQuant(models.Model):
    _inherit = 'stock.quant'

    warehouse_id = fields.Many2one("stock.warehouse")

    @api.model
    def _get_inventory_fields_create(self):
        res = super(InheritStockQuant, self)._get_inventory_fields_create()
        res.append('warehouse_id')
        return res
