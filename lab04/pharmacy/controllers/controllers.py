# -*- coding: utf-8 -*-
# from odoo import http


# class CarRental(http.Controller):
#     @http.route('/car_rental/car_rental', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_rental/car_rental/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_rental.listing', {
#             'root': '/car_rental/car_rental',
#             'objects': http.request.env['car_rental.car_rental'].search([]),
#         })

#     @http.route('/car_rental/car_rental/objects/<model("car_rental.car_rental"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_rental.object', {
#             'object': obj
#         })


# from odoo import http
# from odoo.http import request

# class PharmacySalesController(http.Controller):
#     @http.route('/pharmacy/sales', auth='public', website=True, type='json', methods=['GET'])
#     def index(self, **kw):
#         return request.env['pharmacy.sales'].search([])
#         return http.request.render('your_module.sales_listing', {'sales': sales})

#     @http.route('/pharmacy/sales/<int:sale_id>', auth='public')
#     def sale_details(self, sale_id, **kw):
#         return  request.env['pharmacy.sales'].browse(sale_id)
#         return http.request.render('your_module.sale_details', {'sale': sale})

# from odoo import http
# import json
# from datetime import date

# class PharmacySalesController(http.Controller):
#     @http.route('/pharmacy/sales', auth='public', website=False, type='http', methods=['GET'], csrf=False)
#     def get_pharmacy_sales(self, **kwargs):
#         # Your logic to retrieve the pharmacy sales data goes here
#         data = {'result': 'Pharmacy Sales', 'date': str(date.today())}
#         response = http.Response(json.dumps(data), content_type='application/json')
#         return response
from odoo import http
import json

class PharmacySalesController(http.Controller):
    @http.route('/pharmacy/sales', auth='public', website=False, type='http', methods=['GET'], csrf=False)
    def get_pharmacy_sales(self, **kwargs):
        # Your logic to retrieve the pharmacy sales data goes here
        Medicine = http.request.env['pharmacy.medicines']
        medicines = Medicine.search([])
        
        data = {'medicines': []}
        for medicine in medicines:
            data['medicines'].append({
                'name': medicine.name,
                'type': medicine.type,
                'price': medicine.price,
                'expiration_date': str(medicine.expiration_date),
                'stock': medicine.stock,
            })
        
        response = http.Response(json.dumps(data), content_type='application/json')
        return response
