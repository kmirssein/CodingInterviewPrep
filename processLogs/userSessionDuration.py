def processEvents(logs: list[str], maximumTime: int) -> list[str]:
    """
    Inputs:
        logs: list of strings, each in the format "<user> <timestamp> <sign-in/sign-out>"
        maximumTime: integer maximum allowed session duration.

    Returns:
        list of user IDs (strings) who had sessions with duration <= maximumTime.
        The list is sorted numerically.
    """


    """ 
    Phase 1: Clarify the Problem Statement 
    
    Input: 
    logs: list of strings where each string is formatted "<user_id> <timestamp> <sign-in|sign-out>"
    maximumTime: integer, the maximum allowed session duration
    
    Output: 
    list of strings of user IDs that have a short session duration, sorted in ascending order
    
    What is being asked? 
    1. Parse each log entry to extract user, timestamp, and action
    2. Sort all events by timestamp (because logs may not be in order)
    3. For each user:
        - store their sign-in timestamp
        - when they sign out, compute the session duration
    4. If the duration <= maximumTime, include the user in the output list
    5. Return the list of qualifying users sorted numerically as strings
    
    Constraints: 
    - Logs may be out of order → must sort by timestamp
    - Timestamps must be parsed to integers
    - Each user will have exactly one sign-in before a sign-out
    - Multiple users may interleave their events
    - Output must be sorted numerically (as strings)
    
    Example: 
    20 30 sign-in 
    20 35 sign-out 
    
    output: 
    ["20"]
    
    __________________________________________________________________________________________________________________
     
    Phase 2: Algorithm of the solution 
        
    1. Create an empty list called events to store parsed logs.
    2. Loop through each string in logs:
       - Split the string into user_id, timestamp_str, and action.
       - Convert timestamp_str to an integer.
       - Append a tuple (timestamp, user_id, action) to events.
    3. Sort events by timestamp (the first element of each tuple).
    
    4. Create an empty dictionary login_times to map user_id → sign-in timestamp.
    5. Create an empty set short_users to store user_ids that had a short session.
    
    6. Loop through each (timestamp, user_id, action) in events:
       - If action is "sign-in":
           - Store login_times[user_id] = timestamp.
       - Else (action is "sign-out"):
           - Look up the sign-in time: start = login_times[user_id].
           - Compute duration = timestamp - start.
           - If duration <= maximumTime, add user_id to short_users.
           - Remove this user_id from login_times (since this session is done).
    
    7. Convert short_users (the set) to a list.
    8. Sort this list of user_ids numerically (as strings).
    9. Return the sorted list.
    """

    # step 1
    events = []

    # step 2
    for log in logs:
        user_id, timestamp_str, action = log.split()
        timestamp = int(timestamp_str)
        events.append((timestamp, user_id, action))

    # step 3
    events.sort()

    # step 4
    login_times = {}

    # step 5
    short_users = set()

    # step 6
    for timestamp, user_id, action in events:
        if action == "sign-in":
            login_times[user_id] = timestamp
        else:
            start = login_times[user_id]
            duration = timestamp - start
            if duration <= maximumTime:
                short_users.add(user_id)
            login_times.pop(user_id, None)

    # step 7
    short_users_list = list(short_users)

    # step 8
    short_users_list.sort(key=int)

    # step 9
    return short_users_list

