import json

def handle_json(json_data):
    try:
        data = json.loads(json_data)
        required = ["invoice_id", "amount"]
        missing = [key for key in required if key not in data]
        return {"status": "OK" if not missing else "Missing", "missing_fields": missing}
    except json.JSONDecodeError:
        return {"status": "Invalid JSON"}