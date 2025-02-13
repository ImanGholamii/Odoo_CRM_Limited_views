from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def message_post(self, **kwargs):
        message = f"New opportunity: {self.name}"
        if self.partner_id:
            message += f"\nCustomer: {self.partner_id.name}"

        return super(CrmLead, self).message_post(body=message, **kwargs)

    def message_track(self, tracked_fields, initial_values):
        """delete expected_revenue from log chatter"""

        if 'partner_id' in tracked_fields:
            tracked_fields = {'partner_id'}
        else:
            tracked_fields = set()
        return super(CrmLead, self).message_track(tracked_fields, initial_values)
