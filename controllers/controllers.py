# -*- coding: utf-8 -*-
# from odoo import http


# class LatihanGilang(http.Controller):
#     @http.route('/latihan_gilang/latihan_gilang/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan_gilang/latihan_gilang/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan_gilang.listing', {
#             'root': '/latihan_gilang/latihan_gilang',
#             'objects': http.request.env['latihan_gilang.latihan_gilang'].search([]),
#         })

#     @http.route('/latihan_gilang/latihan_gilang/objects/<model("latihan_gilang.latihan_gilang"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan_gilang.object', {
#             'object': obj
#         })
