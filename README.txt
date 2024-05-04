The Open Voting Machine(OVM) is envisioned to contain the following.
1. an Open Unique Identification system(possibly MOSIP), to identify the citizen, based on which an account is created.
2. An Administrator system, which is expected to be used by Election Commission to manage contesting candidate details, Voting Period, Result date, etc.
3. A voting machine, which enables the registered citizens to vote for the candidate from the list of candidates in the specific constituency

Use cases:
----------
Citizen Registration:
1. Using the registration portal, any citizen satisfying the criteria approved by the Election Commission, shall create an account or ID, by providing requisite information.
2. The User information must be maintained as per the highest standards of protection available. The Personally Identifiable Information must be handled with utmost care. The process shall be in compliance with the local laws of the country conducting the elections.
3. On successful registration, an account is created for the user, which could be used by the user to login and cast their vote.

Administration:
1. The Election Authority of the state, which is conducting the elections shall be provided with options to upload the details of candidates for each constituency for each election(Local body, State Assembly, House of Commons, etc.), involving the following steps.
  a. Candidate registration:
    1. The candidates are registered by the Election Authority under a constituency for an election.
    2. Each candidate is identified using a unique ID using the Open Identification System(possibly MOSIP)
  b. Election Schedule:
    1. Election Authority would schedule the election for each election and each constituency as per its plan.
    2. It can schedule such as a date for the election for constituency, the result announcement date, etc.

Voting Process:
1. On the scheduled date of elections, the registered user may login to the voting portal, and cast or deny to cast their vote to the candidates of their constituency.
2. Once the vote is cast, only the casted vote is stored in a secure "voting database", alongwith the timestamp for verification purpose.(opaque)
3. In order to maintain the secrecy of the voter, Information about the voter is neither read, nor stored, nor transmitted.
4. Once the vote is cast, the opportunity to cast vote is immediately closed, to avoid multiple casting by the same user. This can be achieved by storing the state of the voter for the given election in a "attendance database", which is separate from that of the voting database.(transparent)
5. Care should be taken not to rely on browser features to restrict the voter from casting multiple votes for the same election both within and across constituencies.

Announcement of election results:
1. On the scheduled date for publication of the results, the votes are counted and the results of winning candidates of each constituency for each election is published.

