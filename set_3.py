'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
def relationship_status(from_member, to_member, social_graph):

# Does from_member follow to_member?
    from_follows_to = to_member in social_graph.get(from_member, {}).get("following", [])
    # Does to_member follow from_member?
    to_follows_from = from_member in social_graph.get(to_member, {}).get("following", [])

    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''

  def tic_tac_toe(board):
    
    n = len(board)

    # Helper function to check if all values in a list are the same and not empty
    def all_same(line):
        return line.count(line[0]) == n and line[0] != ""

    # Check rows
    for row in board:
        if all_same(row):
            return row[0]

    # Check columns
    for col in range(n):
        column = [board[row][col] for row in range(n)]
        if all_same(column):
            return column[0]

    # Check main diagonal
    main_diag = [board[i][i] for i in range(n)]
    if all_same(main_diag):
        return main_diag[0]

    # Check anti-diagonal
    anti_diag = [board[i][n - 1 - i] for i in range(n)]
    if all_same(anti_diag):
        return anti_diag[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
def eta(first_stop, second_stop, route_map):

 # If the shuttle is already at the destination
    if first_stop == second_stop:
        return 0

    # Build a quick lookup: start_stop -> (end_stop, travel_time)
    next_leg = {
        start: (end, data['travel_time_mins'])
        for (start, end), data in route_map.items()
    }

    total_time = 0
    current_stop = first_stop

    # Traverse the circular route until the destination is reached
    while True:
        if current_stop not in next_leg:           # safety check (should not occur)
            return None                           # or raise an error

        next_stop, travel_time = next_leg[current_stop]
        total_time += travel_time

        if next_stop == second_stop:              # destination reached
            return total_time

        current_stop = next_stop                  # continue to the next leg
