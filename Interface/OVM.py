from flask import Flask, request, jsonify
from VotingSystem import VotingSystem

app = Flask(__name__)
voting_system = VotingSystem()

@app.route('/login', methods=['POST'])
def login():
    user_id = request.json.get('user_id')
    return voting_system.login(user_id)

@app.route('/logout', methods=['POST'])
def logout():
    user_id = request.json.get('user_id')
    return voting_system.logout(user_id)

@app.route('/castVote', methods=['POST'])
def cast_vote():
    user_id = request.json.get('user_id')
    candidate = request.json.get('candidate')
    constituency = request.json.get('constituency')
    election_type = request.json.get('election_type')
    return voting_system.cast_vote(user_id, candidate, constituency, election_type)

if __name__ == '__main__':
    app.run(debug=True)