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


class pit_attendance(models.Model):

    _name = "pit.attendance"
    _description = "Attendance"

    _sql_constraints = [
                         ('unique_calendar', 
                          'unique(name)',
                          'Choose another value - it has to be unique!')
    ]



    name = fields.Many2one('pit.calendar', string='Calendar', required=True )
    state = fields.Selection([('draft','draft'),('start','start'),('done','done'),('cancel','cancel')], 'State' )
    teacher_id = fields.Many2one('pit.teacher', string='Teacher',related="name.teacher_id",store=True)
    group_id = fields.Many2one('pit.school.course.group', string='Group',related="name.group_id",store=True)
    attendance_line_ids = fields.One2many('pit.attendance.line', 'attendance_id',string='Lines')

    active = fields.Boolean('Active', default=True)

    @api.one
    def do_start(self):
        lines =[]
        for enroll in self.group_id.enrollment_ids :
            if enroll.state == 'active':
                self.env['pit.attendance.line'].create({'attendance_id':self.id,'student_id':enroll.student_id.id,'attendance_state':'0'})
        self.state = 'start'


class pit_attendance_line(models.Model):

    _name = "pit.attendance.line"
    _description = "Attendance"
    _order = "student_id"
    _sql_constraints = [
                         ('unique', 
                          'unique(student_id,attendance_id)',
                          'Choose another value - it has to be unique!')
    ]


    attendance_id = fields.Many2one('pit.attendance', 'Attendance', required=True )
    student_id = fields.Many2one('pit.student', 'Student', required=True )
    attendance_state = fields.Selection([('1','Presente'),('0.5','Tarde'),('0','Ausente')], string='State',default='0', required=True )
    attendance_value = fields.Float( 'Attendance', store=True,compute='_compute_attendande_value')
    
    @api.multi
    @api.depends('attendance_state')
    @api.onchange('attendance_state')
    def _compute_attendande_value(self):
        for line in self:
            if line.attendance_state :
                line.attendance_value = float(line.attendance_state)
