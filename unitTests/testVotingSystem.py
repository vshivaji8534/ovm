import unittest
from VotingSystem import VotingSystem

class TestVotingSystem(unittest.TestCase):
    def setUp(self):
        self.voting_system = VotingSystem()
        self.user_id = "user123"
        self.constituency = "Constituency A"
        self.election_type = "Local body"

    def test_login_and_cast_vote_success(self):
        candidate = "Alice"
        self.voting_system.login_and_cast_vote(self.user_id, candidate, self.constituency, self.election_type)
        self.assertTrue(self.voting_system.voting_database.get(self.user_id))

    def test_login_and_cast_vote_multiple_voting_attempt(self):
        candidate1 = "Alice"
        candidate2 = "Bob"
        self.voting_system.login_and_cast_vote(self.user_id, candidate1, self.constituency, self.election_type)
        self.voting_system.login_and_cast_vote(self.user_id, candidate2, self.constituency, self.election_type)
        self.assertEqual(len(self.voting_system.voting_database), 1)

if __name__ == '__main__':
    unittest.main()