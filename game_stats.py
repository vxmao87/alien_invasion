from pathlib import Path


class GameStats:
    def __init__(self, ai_game):
        """
        Initializes statistics.
        """
        self.settings = ai_game.settings
        self.reset_stats()

        # High scores should never be reset.
        self.high_score = self._obtain_high_score()

    
    def _obtain_high_score(self):
        """
        Obtains the current high score.
        """
        score_path = Path("high_score.txt")
        return int(score_path.read_text().rstrip())


    def reset_stats(self):
        """
        Initializes statistics that can change during the game.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1