class ElectionAuthority:

    def __init__(self):
        self.candidates = {}

    def register_candidate(self, candidate_name, constituency, election_type):
        candidate_id = f"{constituency}_{election_type}_{len(self.candidates) + 1}"
        self.candidates[candidate_id] = {
            "name": candidate_name,
            "constituency": constituency,
            "election_type": election_type
        }
        print("Candidate registered successfully. Candidate ID:", candidate_id)

    def schedule_election(self, constituency, election_type, election_date,
                          result_announcement_date):
        print(f"Election scheduled for {constituency} - {election_type}")
        print(f"Election date: {election_date}")
        print(f"Result announcement date: {result_announcement_date}")

    def announce_election_results(self, election_type):
        # Implement code to count votes and announce results for the given election type
        print(f"Announcing election results for {election_type} elections")


# Example usage
#election_authority = ElectionAuthority()
#election_authority.register_candidate("Alice", "Constituency A", "Local body")
#election_authority.register_candidate("Bob", "Constituency B", "State Assembly")
#election_authority.schedule_election("Constituency A", "Local body", "2023-05-15", "2023-05-16")
