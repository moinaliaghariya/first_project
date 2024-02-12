from odoo import api, fields, models
import datetime


class StudentInfo(models.Model):
    _name = "student.info"
    _description = "studentInfo"

    name = fields.Char(string="Name")
    roll_no = fields.Integer(string="Roll No")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age")
    standard_id = fields.Many2one("class.detail" ,string="Standard")
    division = fields.Char(related="standard_id.division" ,string="Division")
    sub_english = fields.Boolean(string="English",compute="_compute_subject")
    sub_math = fields.Boolean(string="Maths", compute="_compute_subject")
    sub_hindi = fields.Boolean(string="Hindi",compute="_compute_subject")


    def _compute_subject(self):
        for rec in self:
            rec.sub_english=False
            rec.sub_math=False
            rec.sub_hindi=False
            sub_english = (rec.standard_id.teacher_ids.filtered
                           (lambda teacher: teacher.subject == "English"))
            english_teacher = (sub_english.attendance_ids.filtered
                               (lambda teacher_attendance_id: teacher_attendance_id.checkedin and teacher_attendance_id.checkedin.date() == datetime.datetime.today().date()))
            for today_attendance in english_teacher:
                if today_attendance.checkedin and not today_attendance.checkedout:
                    rec.sub_english = True
                else:
                    rec.sub_english = False

            sub_math = (rec.standard_id.teacher_ids.filtered
                        (lambda teacher: teacher.subject == "Maths"))
            math_teacher = (sub_math.attendance_ids.filtered
                            (lambda teacher_attendance_id: teacher_attendance_id.checkedin and teacher_attendance_id.checkedin.date() == datetime.datetime.today().date()))
            for today_attendance in math_teacher:
                if today_attendance.checkedin and not today_attendance.checkedout:
                    rec.sub_math = True
                else:
                    rec.sub_math = False

            sub_hindi = (rec.standard_id.teacher_ids.filtered
                         (lambda teacher: teacher.subject == "Hindi"))
            hindi_teacher = (sub_hindi.attendance_ids.filtered
                             (lambda teacher_attendance_id: teacher_attendance_id.checkedin and teacher_attendance_id.checkedin.date() == datetime.datetime.today().date()))
            for today_attendance in hindi_teacher:
                if today_attendance.checkedin and not today_attendance.checkedout:
                    rec.sub_hindi = True
                else:
                    rec.sub_hindi = False

