app_name = "purchase_broker"
app_title = "Purchase Broker"
app_publisher = "Your Name"
app_description = "Custom app for managing purchase broker contracts"
app_email = "email@example.com"
app_license = "MIT"

app_include_js = []
app_include_css = []

doc_events = {
    "Purchase Receipt": {
        "validate": "purchase_broker.purchase_broker.events.validate_against_contract",
        "on_submit": "purchase_broker.purchase_broker.events.update_supplied_qty"
    },
    "Purchase Invoice": {
        "validate": "purchase_broker.purchase_broker.events.validate_against_contract",
        "on_submit": "purchase_broker.purchase_broker.events.update_supplied_qty"
    }
}
