import frappe
def get_context(context):
    context.sips = frappe.get_list("SIP", fields=["fund_name", "frequency", "amount"])



