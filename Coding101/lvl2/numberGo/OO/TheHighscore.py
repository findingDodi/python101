import os
from TheScore import TheScore


class TheHighscore:

    def __init__(self):
        self.highscore_file = "highscores.txt"

        self.list_of_scores = []
        self.set_list_of_scores()

    def set_list_of_scores(self):
        if not os.path.isfile(self.highscore_file):
            return

        file_handle = open(self.highscore_file, "r")
        file_lines = file_handle.readlines()

        for line in file_lines:
            single_parts = line.rstrip().split(";")
            self.list_of_scores.append(TheScore(single_parts[0], int(single_parts[1])))

        file_handle.close()

    def save_highscore(self, user_name, user_score):
        score_info = TheScore(user_name.strip(), user_score)
        self.list_of_scores.append(score_info)

        if len(self.list_of_scores) > 1:
            self.list_of_scores.sort(key=lambda x: x.score, reverse=True)

        best_of_five = self.list_of_scores[0:5]

        file_handle = open(self.highscore_file, "w")

        highscore: TheScore
        for highscore in best_of_five:
            score_info = "{};{}\n".format(highscore.get_name(), highscore.get_score())
            file_handle.write(score_info)

        file_handle.close()

    def print_highscores(self):
        if len(self.list_of_scores):
            print("Here are the current Highscores:")

            score: TheScore
            for score in self.list_of_scores:
                print("{}{}".format(score.get_name().ljust(20, " "), str(score.get_score()).rjust(3, " ")))

        print("#" * 20)
