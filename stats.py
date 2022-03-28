class Stats:
    """отслеживаниее статистики"""

    def __init__(self):
        """инициализирует статистику"""

        self.run_game = True
        self.reset_stats()
        with open('high_core.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        """статистика изменяющая во время игры"""
        self.score = 0
        self.guns_life = 3
