# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritStockQuant(models.Model):
    _inherit = 'stock.quant'

    get_warehouse = fields.Many2one("stock.warehouse", compute="_get_warehouse_id")
    warehouse_id = fields.Many2one("stock.warehouse")

    @api.depends('location_id', 'product_id', 'warehouse_id')
    def _get_warehouse_id(self):
        self.warehouse_id = self.location_id.warehouse_id.ids[0] if len(
            self.location_id.warehouse_id.ids) > 1 else self.location_id.warehouse_id.id
        # self.warehouse_id = self.location_id.warehouse_id.ids[0] if len(
        #     self.location_id.warehouse_id.ids) > 1 else self.location_id.warehouse_id.id
        self.get_warehouse = 1

    @api.model
    def _get_inventory_fields_create(self):
        res = super(InheritStockQuant, self)._get_inventory_fields_create()
        res.append('warehouse_id', 'get_warehouse')
        return res
