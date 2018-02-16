# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from openerp import tools

from openerp.tools.translate import _

import logging

_logger = logging.getLogger(__name__)




class pit_calendar_attendance(models.Model):

    _name = "pit.calendar.attendance"
    _description = "Attendance"
    _order = "student_id"
    _sql_constraints = [
                         ('unique', 
                          'unique(student_id,calendar_id)',
                          'Choose another value - it has to be unique!')
    ]


    calendar_id = fields.Many2one('pit.calendar', 'Calendar', required=True )
    enrollment_id = fields.Many2one('pit.enrollment', 'Enrollment', required=True )

    student_id = fields.Many2one('pit.student', 'Student', required=True )

    attendance_present = fields.Boolean('P')
    attendance_late = fields.Boolean('T')
    
    #attendance_state = fields.Selection([('1','Presente'),('0.5','Tarde'),('0','Ausente')], string='State',default='0', required=True )
    attendance_value = fields.Float( 'Attendance', store=True,compute='_compute_attendande_value')
    
    @api.multi
    @api.depends('attendance_present','attendance_late')
    @api.onchange('attendance_present','attendance_late')
    def _compute_attendande_value(self):
        for line in self:
            if line.attendance_present :
                line.attendance_value = 1.0
            elif line.attendance_late :
                line.attendance_value = 0.5
            else:
                line.attendance_value = 0

