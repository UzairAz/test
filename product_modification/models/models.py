# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductType(models.Model):
    _name = "product.type"
    _description = "Product Type"
    _rec_name = 'name'

    name = fields.Char("Name")


class ProductSegment(models.Model):
    _name = "product.segment"
    _description = "Product Segment"
    _rec_name = 'name'

    name = fields.Char("name")


class InheritProductModel(models.Model):
    _inherit = 'product.product'

    m_type = fields.Many2one('product.type', string='Type')
    segment = fields.Many2one('product.segment', string="Segment")


class _InheritProductTempModel(models.Model):
    _inherit = 'product.template'

    m_type = fields.Many2one('product.type', string='Type')
    segment = fields.Many2one('product.segment', string="Segment")

    @api.model
    def create(self, vals):
        res = super(_InheritProductTempModel, self).create(vals)
        product_product = self.env['product.product'].search([('product_tmpl_id', '=', res.id)])
        if product_product:
            for rec in product_product:
                rec.m_type = res.m_type.id
                rec.segment = res.segment.id
        return res
