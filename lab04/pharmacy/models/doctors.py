# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Doctors(models.Model):
    _name = 'pharmacy.doctors'
    _description = 'pharmacy doctors'

    id = fields.Char(string='Id', required=True)
    name = fields.Char(string='Doctors', required=True, default='N/A')
    salary = fields.Float(string='Salary', required=True)
    age = fields.Char(string='Age', required=True)
    shift = fields.Selection(selection=[
        ('day', 'day'), 
        ('night', 'night')]
        ,string='shift', required=True)

    start_date = fields.Date(string='Doctor start date', required=True)
    image = fields.Image(string='Doctor Image', required=True)
    note = fields.Text(string='Doctor Notes')
    # year = fields.Integer(string='Car Year', required=True)
    # sale_ids = fields.One2many(comodel_name='car.rental.sales', inverse_name='car', string='Sales')



