
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PharmacySales(models.Model):
    _name = 'pharmacy.sales'
    _description = 'Pharmacy Sales'

    number = fields.Char(string='Sales Number', required=True)
    medicine = fields.Many2one(comodel_name='pharmacy.medicines', string='Medicine', required=True)
    doctor = fields.Many2one(comodel_name='pharmacy.doctors', string='Doctor', required=True)
    date = fields.Date(string='Date', required=True)
    price = fields.Float(string='Price', required=True)
    customer = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    
