import time


class VotingSystem:

    def __init__(self):
        self.voting_database = {}
        self.attendance_database = {}

    def login_and_cast_vote(self, user_id, candidate, constituency,
                            election_type):
        if self.attendance_database.get(user_id, {}).get(election_type, False):
            print(
                "You have already cast your vote for this election. Multiple voting is not allowed."
            )
        else:
            timestamp = time.time()  # Get current timestamp
            self.voting_database[user_id] = {
                "candidate": candidate,
                "constituency": constituency,
                "election_type": election_type,
                "timestamp": timestamp
            }
            self.attendance_database.setdefault(user_id, {}).update(
                {election_type: True})
            print("Vote cast successfully for candidate:", candidate)


# Example usage
#voting_system = VotingSystem()
#user_id = "user123"
#constituency = "Constituency A"
#election_type = "Local body"
#voting_system.login_and_cast_vote(user_id, "Alice", constituency, election_type)
#voting_system.login_and_cast_vote(user_id, "Bob", constituency, election_type)  # Try to cast multiple votes
