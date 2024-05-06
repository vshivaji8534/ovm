from flask import Flask, request, jsonify
from CitizenRegistration import CitizenRegistration
import uuid

app = Flask(__name__)
citizen_registration = CitizenRegistration()

@app.route('/register', methods=['POST'])
def register_citizen():
    data = request.json
    unique_id = str(uuid.uuid4())
    citizen_data = {
        "name": data.get("name"),
        "age": data.get("age"),
        "country": data.get("country"),
        "mosip_id": unique_id
    }

    citizen_registration.register_citizen(citizen_data)
    
    return jsonify({"mosip_id": unique_id, "message": "Citizen registered successfully"})

@app.route('/unregister', methods=['POST'])
def unregister_citizen():
    mosip_id = request.json.get("mosip_id")
    success = citizen_registration.unregister_citizen(mosip_id)
    
    if success:
        return jsonify({"message": "Citizen unregistered successfully"})
    else:
        return jsonify({"error": "Citizen with provided MOSIP ID not found"})

if __name__ == '__main__':
    app.run(debug=True)