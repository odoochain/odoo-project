from odoo import models, fields, api, _


class ProjectProject(models.Model):
    _inherit = 'project.project'

    external_id = fields.Char(string="External ID")


class ProjectTask(models.Model):
    _inherit = 'project.task'

    external_id = fields.Char(string="External ID")
