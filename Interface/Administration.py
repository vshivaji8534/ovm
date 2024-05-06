from flask import Flask, request, jsonify
from ElectionAuthority import ElectionAuthority

app = Flask(__name__)
election_authority = ElectionAuthority()

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    return election_authority.login(username, password)

@app.route('/logout', methods=['POST'])
def logout():
    # Implement logout logic here
    return "Logout Successful"

@app.route('/updateElections', methods=['POST'])
def update_elections():
    election_data = request.json
    # Implement update elections logic here
    return "Elections Updated Successfully"

@app.route('/updateConstituencies', methods=['POST'])
def update_constituencies():
    constituency_data = request.json
    # Implement update constituencies logic here
    return "Constituencies Updated Successfully"

@app.route('/updateCandidates', methods=['POST'])
def update_candidates():
    candidate_data = request.json
    # Implement update candidates logic here
    return "Candidates Updated Successfully"

if __name__ == '__main__':
    app.run(debug=True)