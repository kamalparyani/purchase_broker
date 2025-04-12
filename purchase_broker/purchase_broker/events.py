import frappe

def validate_against_contract(doc, method):
    if not doc.get("purchase_broker_contract"):
        return

    contract = frappe.get_doc("Purchase Broker Contract", doc.purchase_broker_contract)
    contract_items = {item.item_code: item for item in contract.contract_items}

    for item in doc.items:
        if item.item_code not in contract_items:
            frappe.throw(f"Item {item.item_code} not found in contract {contract.name}.")

        contract_item = contract_items[item.item_code]
        total_supplied = contract_item.supplied_qty or 0
        pending = contract_item.contract_qty - total_supplied

        if item.qty > pending:
            frappe.throw(f"Cannot supply {item.qty} of {item.item_code}. Only {pending} pending in contract {contract.name}.")

def update_supplied_qty(doc, method):
    if not doc.get("purchase_broker_contract"):
        return

    contract = frappe.get_doc("Purchase Broker Contract", doc.purchase_broker_contract)
    for item in contract.contract_items:
        supplied = frappe.db.sql("""
            SELECT SUM(qty) FROM `tabPurchase Receipt Item` pri
            JOIN `tabPurchase Receipt` pr ON pri.parent = pr.name
            WHERE pr.docstatus = 1 AND pri.item_code = %s
            AND pr.purchase_broker_contract = %s
        """, (item.item_code, contract.name))[0][0] or 0

        item.supplied_qty = supplied
        item.pending_qty = item.contract_qty - supplied
    contract.save()
