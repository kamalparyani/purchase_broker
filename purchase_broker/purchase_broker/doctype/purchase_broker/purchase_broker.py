import frappe
from frappe.model.document import Document

class PurchaseBroker(Document):
    def validate(self):
        if self.email and "@" not in self.email:
            frappe.throw("Please enter a valid email address.")
