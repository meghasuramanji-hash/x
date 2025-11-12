from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

DATA_FILE = "records.json"

# ✅ Load data
def load_records():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# ✅ Save data
def save_records(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# ✅ API: Get all health records
@app.route("/api/records", methods=["GET"])
def get_records():
    return jsonify(load_records())


# ✅ API: Save a new record
@app.route("/api/records", methods=["POST"])
def add_record():
    record = request.json
    records = load_records()
    records.append(record)
    save_records(records)
    return jsonify({"message": "Record saved!", "status": "success"})


# ✅ API: Chatbot backend (optional – for more realistic replies)
@app.route("/api/bot", methods=["POST"])
def bot_reply():
    user_msg = request.json.get("message", "").lower()

    # Simple backend logic
    if "fever" in user_msg:
        return jsonify({
            "reply": "It seems like you have fever. Drink warm water and take Paracetamol 500mg."
        })

    if "chest pain" in user_msg:
        return jsonify({
            "reply": "⚠️ Chest pain can be serious. Please call your caregiver or ambulance immediately."
        })

    return jsonify({
        "reply": "I understand. Could you describe your symptoms clearly?"
    })


if __name__ == "__main__":
    app.run(debug=True)
