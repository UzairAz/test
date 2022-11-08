# -*- coding: utf-8 -*-


from odoo import api, models


class SalesByCustomer(models.AbstractModel):
    _name = 'report.sales_report_by_customer.sales_report_customer'
    _description = 'Get Sales Report By Customer'

    def get_tax(self, line=None):
        total_tax = 0
        for tax in line.tax_ids:
            total_tax += line.price_subtotal * (tax.amount / 100)
        return total_tax

    @api.model
    def _get_report_values(self, docids, data=None):
        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        selected_id_list = data['form']['selected_id_list']
        selected_user_id_list = data['form']['selected_user_id_list']
        if data['form']['report_for'] == 'customer':
            customers = self.env['account.move'].search([('partner_id', 'in', selected_id_list)])
        else:
            customers = self.env['account.move'].search([('invoice_user_id', 'in', selected_user_id_list)])

        data_list = []

        for partner in list(set(customers.mapped('partner_id.id'))) if data['form'][
                                                                           'report_for'] == 'customer' else list(
            set(customers.mapped('invoice_user_id.id'))):
            if data['form']['report_for'] == 'customer':
                invoice_search = self.env['account.move'].search(
                    [('partner_id', '=', partner), ('invoice_date', '>=', date_from),
                     ('invoice_date', '<=', date_to), ('state', '=', 'posted'), ('move_type', '=', 'out_invoice')])
            else:
                invoice_search = self.env['account.move'].search(
                    [('invoice_user_id', '=', partner), ('invoice_date', '>=', date_from),
                     ('invoice_date', '<=', date_to), ('state', '=', 'posted'), ('move_type', '=', 'out_invoice')])

            current_dic = {}
            if invoice_search:
                current_dic.update({
                    'customer': invoice_search[0].partner_id.name,
                    'sale_person': invoice_search[0].invoice_user_id.name,
                    "invoices": []
                })
                i = 0
                for inv in invoice_search:
                    current_dic["invoices"].append({
                        "invoice": inv,
                        "lines": []
                    })
                    for line in inv.invoice_line_ids:
                        current_dic["invoices"][i]['lines'].append({
                            'product_id_name': line.product_id.name,
                            'product_qty': line.quantity,
                            'price_subtotal': line.price_subtotal,
                            'tax_amount': self.get_tax(line),
                            'total_tax': self.get_tax(line),
                            'untax_total_amount': inv.amount_untaxed,
                            'amount_total': inv.amount_total,
                            "price_unit": line.price_unit,
                        })
                    i += 1
                data_list.append(current_dic)

        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))

        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'data': data_list,
            'docs': docs,
            'date_to': date_to,
            'date_from': date_from,
            'report_for': data['form']['report_for']
        }
