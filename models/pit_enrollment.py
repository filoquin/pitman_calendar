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
from datetime import datetime , timedelta , date
from dateutil.relativedelta import relativedelta

from openerp.tools.translate import _

import logging

_logger = logging.getLogger(__name__)

class pit_enrollment(models.Model):

    _inherit = "pit.enrollment"

    attendance = fields.Float('Attendance', 'compute_attendance')
    attendance_rate = fields.Float('Attendance rate', 'compute_attendance')

    @api.multi
    @api.depends('group_id')
    def compute_attendance(self):
        expected_attendance = self.env['pit.calendar'].search_count([('group_id','=',self.id),('start_date','<',fields.Datetime.Today())])
        #att = self._cr.execute("SELECT student_id,sum(attendance_value) FROM pit_attendance_line where gro")

        #for enroll in self:

