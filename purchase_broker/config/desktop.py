from frappe import _

def get_data():
    return [
        {
            "module_name": "purchase_broker",
            "label": _("Purchase Broker"),
            "color": "blue",
            "icon": "octicon octicon-person",
            "type": "module",
            "link": "List/Purchase Broker/List"
        }
    ]
