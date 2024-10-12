import chess

PAWN = 1
KNIGHT = 3
BISHOP = 3
ROOK = 5
QUEEN = 9
KING = 0 # NaN error if float('inf) is used

piece_map = {
    chess.KING: KING,
    chess.QUEEN: QUEEN,
    chess.ROOK: ROOK,
    chess.BISHOP: BISHOP,
    chess.KNIGHT: KNIGHT,
    chess.PAWN: PAWN,
}

def eval(board):
    material = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            sign = 1 if piece.color == chess.WHITE else -1
            material += piece_map[piece.piece_type] * sign
    return material