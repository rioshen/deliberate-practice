#!/usr/bin/env python
"""Problem from topcoder.
Problem statement: The game is played on a 8x8 grid with two players, Black
and Red. The players alternate turns placing one piece representing their
color in one empty square of the grid. When the Red player puts a red piece
down, any black pieces that end up between the piece that was placed on the
board and any other red piece already on the board should be changed to red.
If the change in color from black to red of any piece on the board causes
other black pieces to lie between two red pieces, those black pieces should
also be changed to red.

NOTES
- redPieces is a String[] representing the current positions of red pieces on
the board.
- blackPieces is a String[] representing the current positions of black pieces
on the board.
- The board is an 8x8 grid with the columns referred to by the uppercase
letters A-H and the rows referred to by the numbers 1-8 (inclusive).  The
column is specified before the row.  A1 is in the upper left.  H8 is in the
lower right.
- redPieces and blackPieces are not necessarily the same length (players may
have passed on moves).
- A black piece is between two red pieces if a red piece can be found before an
empty square on either side by following the horizontal, vertical, or either
diagonal out from the Black piece.  For example:

- - - R - - - -
- - - B - - - -
- - - B - - - -    All three Black pieces are between two red pieces.
- - - B - - - -
- - - R - - - -


- - - R - - - -
- - - B B - - -
- - - B - B - -   All four Black pieces are between two Red pieces.
- - - R R R R R


- - - R - - - -
- - - B R - - -
- - - - - - - -   The Black piece is not between two Red pieces.
- - - R R - - -


R R R R R R R R
R - - - - - - R
R - B B - B - R
R - B B B B - R   None of the Black pieces are between two Red pieces.
R - - - - - - R
R R R R R R R R
"""
__author__ = 'Rio'


class Tothello(object):
    """Helps a player determine their best possible move - the move that
    results - the move that results in the most pieces being that player's
    color at the end of the move.
    """
    def __init__(self):
        pass

    @staticmethod
    def best_move(red_pieces, black_pieces, whose_turn):
        """
        """
