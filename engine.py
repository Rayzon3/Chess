class GameState():
    def __init__(self):
        self.board = [
            ["bE", "bH", "bB", "bQ", "bK", "bB", "bH", "bE"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wE", "wH", "wB", "wQ", "wK", "wB", "wH", "wE"],]
    
        self.whiteMove = True
        self.moveLog = []