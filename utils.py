def initial_dict() -> dict:
    """
    Generate the game board dictionary. 9 keys (board positions) and
    9 values (initially '-' and will change to 'X' or 'O').
    """

    dic = {'A1': '-', 'A2': '-', 'A3': '-', 'B1': '-', 'B2': '-', 'B3': '-', 'C1': '-', 'C2': '-', 'C3': '-'}

    return dic


def grid_3x3(dic: str) -> str:
    """
    Returns the structure of the game board

    Parameters
    ----------
    dic (str): Dictionary of 9 keys and 9 values. The game board is
    generated from a dictionary of 9 keys and 9 positions.
    """

    print('+' + '--------+' * 3)
    print('|A1:  {}  |B1:  {}  |C1:  {}  |'.format(dic.get('A1'), dic.get('B1'), dic.get('C1')))
    print('+' + '--------+' * 3)
    print('|A2:  {}  |B2:  {}  |C2:  {}  |'.format(dic.get('A2'), dic.get('B2'), dic.get('C2')))
    print('+' + '--------+' * 3)
    print('|A3:  {}  |B3:  {}  |C3:  {}  |'.format(dic.get('A3'), dic.get('B3'), dic.get('C3')))
    print('+' + '--------+' * 3)


def game_winner(dic: str) -> bool:
    """
    Returns if there is a winner in the completed turn.

    Parameters
    ----------
    dic (str): Dictionary of 9 keys and 9 values.
    """
    if (dic['A1'] == dic['A2'] == dic['A3'] != '-' or
            dic['B1'] == dic['B2'] == dic['B3'] != '-' or
            dic['C1'] == dic['C2'] == dic['C3'] != '-' or
            dic['A1'] == dic['B1'] == dic['C1'] != '-' or
            dic['A2'] == dic['B2'] == dic['C2'] != '-' or
            dic['A3'] == dic['B3'] == dic['C3'] != '-' or
            dic['A1'] == dic['B2'] == dic['C3'] != '-' or
            dic['C1'] == dic['B2'] == dic['A3'] != '-'):

        return True

    else:
        return False


def player_turn(dic: str, player: str) -> None:
    """
    Assigns the value 'X' or 'O' to the position chosen by the player.

    Parameters
    ----------
    dic (str): Dictionary of 9 keys and 9 values.
    player (str): Player turn. 'X' or 'O'
    """
    player_in = input()

    while (player_in not in dic.keys() or dic[player_in] != '-'):
        print('ERROR. Enter a new position')
        player_in = input()

    else:
        dic[player_in] = player
