
def handle_email(data):
    sender = "Unknown"
    lines = data.splitlines()
    for line in lines:
        if "From" in line:
            sender = line.split("From:")[1].strip()
    urgency = "High" if "urgent" in data.lower() else "Normal"
    return {"sender":sender , "urgency":urgency}
