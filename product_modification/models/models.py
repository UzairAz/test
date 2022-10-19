# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritProductModel(models.Model):
    _inherit = 'product.product'

    type = fields.Char('Type')
    Segment = fields.Char('Segment')


class _InheritProductTempModel(models.Model):
    _inherit = 'product.template'

    m_type = fields.Char('Type')
    segment = fields.Char('Segment')

    @api.model
    def create(self, vals):
        res = super(_InheritProductTempModel, self).create(vals)
        product_product = self.env['product.product'].search([('product_tmpl_id', '=', res.id)])
        if product_product:
            for rec in product_product:
                rec.m_type = res.type
                rec.segment = res.segment
        return res
