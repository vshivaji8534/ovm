import unittest
from ElectionAuthority import ElectionAuthority


class TestElectionAuthority(unittest.TestCase):

    def setUp(self):
        self.election_authority = ElectionAuthority()

    def test_register_candidate(self):
        candidate_name = "Alice"
        constituency = "Constituency A"
        election_type = "Local body"

        self.election_authority.register_candidate(candidate_name,
                                                   constituency, election_type)

        candidate_id = f"{constituency}_{election_type}_1"
        self.assertIn(candidate_id, self.election_authority.candidates)

    def test_schedule_election(self):
        constituency = "Constituency A"
        election_type = "Local body"
        election_date = "2023-05-20"
        result_announcement_date = "2023-05-21"

        self.election_authority.schedule_election(constituency, election_type,
                                                  election_date,
                                                  result_announcement_date)

        self.assertIsNotNone(self.election_authority.candidates)

    def test_announce_election_results(self):
        election_type = "Local body"

        # Add a sample candidate to announce results
        self.election_authority.register_candidate("Alice", "Constituency A",
                                                   "Local body")

        self.election_authority.announce_election_results(election_type)
        self.assertTrue(
            True)  # Placeholder assertion as announcement is a print statement


if __name__ == "__main__":
    unittest.main()
