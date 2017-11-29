# -*- coding: utf-8 -*-
from openerp import http

# class PitmanCalendar(http.Controller):
#     @http.route('/pitman_calendar/pitman_calendar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pitman_calendar/pitman_calendar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pitman_calendar.listing', {
#             'root': '/pitman_calendar/pitman_calendar',
#             'objects': http.request.env['pitman_calendar.pitman_calendar'].search([]),
#         })

#     @http.route('/pitman_calendar/pitman_calendar/objects/<model("pitman_calendar.pitman_calendar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pitman_calendar.object', {
#             'object': obj
#         })