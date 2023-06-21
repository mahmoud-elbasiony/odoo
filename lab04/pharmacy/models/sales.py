
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PharmacySales(models.Model):
    _name = 'pharmacy.sales'
    _description = 'Pharmacy Sales'

    number = fields.Char(string='Sales Number', required=True)
    medicine = fields.Many2one(comodel_name='pharmacy.medicines', string='Medicine', required=True)
    doctor = fields.Many2one(comodel_name='pharmacy.doctors', string='Doctor', required=True)
    date = fields.Date(string='Date', required=True)
    customer = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    amount=fields.Float(string='amount', required=True) 
    price=fields.Float(string='price', related='medicine.price', required=True) 

    total=fields.Float(string='total', compute="_compute_total" ,store=True) 

    
    @api.depends("amount","medicine")
    def _compute_total(self):
        for record in self:
            record.total=record.medicine.price*record.amount

    @api.onchange("amount","medicine")
    def _onchange_total(self):
        if self.medicine:
            self.total=self.medicine.price*self.amount
