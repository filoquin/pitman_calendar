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
from datetime import datetime , timedelta

from openerp.tools.translate import _

from dateutil.rrule import rrule, DAILY , WEEKLY ,MO



import logging

_logger = logging.getLogger(__name__)


class pit_school_course_group(models.Model):

    _inherit = "pit.school.course.group"

    @api.model
    def create (self,values):
        res = super(pit_school_course_group,self).create(values)
        res.create_calendar()
        return res

    @api.one
    def write (self,values):
        res = super(pit_school_course_group,self).write(values)
        self.create_calendar()
        return res

    @api.one
    def create_calendar(self):

        pit_calendar_items =[]
        for calendar_line in self.calendar_ids :

            date_from = fields.Datetime.from_string(self.date_from)
            date_to = fields.Datetime.from_string(self.date_to)
            if calendar_line.date_from :
                date_from = fields.Datetime.from_string(calendar_line.date_from)
            if calendar_line.date_to :
                date_to = fields.Datetime.from_string(calendar_line.date_to)


            #date_from = min(fields.Datetime.from_string(self.date_from),fields.Datetime.from_string(calendar_line.date_from))
            #date_to = min(fields.Datetime.from_string(self.date_to),fields.Datetime.from_string(calendar_line.date_to))
            for dt in rrule(freq=WEEKLY,byweekday=int(calendar_line.dayofweek), wkst=MO,dtstart=date_from, until=date_to):

                calendar = {}
                #to-do ver tds GTM 
                calendar['start_date']=dt + timedelta(hours =calendar_line.hour_from ) + timedelta(hours =3 )
                calendar['end_date']=dt + timedelta(hours=calendar_line.hour_to )+ timedelta(hours =3 )
                calendar['teacher_id']=calendar_line.teacher_id.id
                calendar['group_id']=self.id
                calendar['group_calendar_id']=calendar_line.id
                
                pit_calendar_items.append(calendar)             

        pit_calendar_items_sorted = sorted(pit_calendar_items, key=lambda k: k['start_date']) 
        i= 0
        for calendar in pit_calendar_items_sorted :
            i += 1

            calendar['class_number'] = i                
            exist = self.env['pit.calendar'].search([('group_id','=',self.id), ('class_number','=',i)], limit=1)
            if len(exist):
                exist.write(calendar)
            else :
                self.env['pit.calendar'].create(calendar)
