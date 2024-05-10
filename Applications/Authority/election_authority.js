class ElectionAuthority {

    constructor() {
        this.candidates = {};
    }

    register_candidate(candidate_name, constituency, election_type) {
        const candidate_id = `${constituency}_${election_type}_${Object.keys(this.candidates).length + 1}`;
        this.candidates[candidate_id] = {
            name: candidate_name,
            constituency: constituency,
            election_type: election_type
        };
        console.log("Candidate registered successfully. Candidate ID:", candidate_id);
    }

    schedule_election(constituency, election_type, election_date, result_announcement_date) {
        console.log(`Election scheduled for ${constituency} - ${election_type}`);
        console.log(`Election date: ${election_date}`);
        console.log(`Result announcement date: ${result_announcement_date}`);
    }

    announce_election_results(election_type) {
        console.log(`Announcing election results for ${election_type} elections`);
    }
}

// Example usage
// const election_authority = new ElectionAuthority();
// election_authority.register_candidate("Alice", "Constituency A", "Local body");
// election_authority.register_candidate("Bob", "Constituency B", "State Assembly");
// election_authority.schedule_election("Constituency A", "Local body", "2023-05-15", "2023-05-16");