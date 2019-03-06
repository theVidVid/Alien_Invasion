def save_high_score(stats, sb):
    """Writes high score to .txt file."""
    saved_high_score = round(stats.high_score, -1)
    high_score_str = "{:,}".format(high_score)
    save_score = "GameSaveData/high_score.txt"
    with open(save_score, 'w') as f_obj:
        f_obj.write(saved_high_score)



        self.load_score = "GameSaveData/high_score.txt"
        with open(self.load_score) as f_obj:
            self.high_score = f_obj.read()
            # ~ self.high_score = round(self.high_score, -1)
            # ~ self.high_score = "{:,}".format(high_score)

            if not self.high_score:
                self.high_score = 0
