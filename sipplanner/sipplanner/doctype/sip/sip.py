# Copyright (c) 2024, Drishya R and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SIP(Document):

	def before_save(self):
		self.display = f'{self.frequency} {self.amount}'
	pass
