# Odoo_CRM_Limited_views
This module customizes the CRM log notes by limiting the displayed information,  to only the opportunity name and customer name, also add limits to show some fields to general users.
The only fields that are tracked are:
```.py
  {'email_from', 'phone', 'team_id', 'lost_reason', 'partner_id', 'expected_revenue', 'type', 'partner_name', 'active', 'stage_id', 'contact_name', 'user_id'}
```
Since the log note is a public section, we have limited the fields to the customer name.

On the other hand, because information such as the customer's email and phone number, which are private, or financial information was displayed on the main opportunity form, we restricted its viewing to public users.
