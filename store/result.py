import constants as const


class Result(object):
    __score = 0
    __life = 3
    __blood = 1000
    # def __init__(self):
    #     self.__score = None

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val):
        if val >= 0:
            self.__score = val

    def get_highest_score(self):
        """
        get the highest score from the result file
        :return: the highest score
        """
        result = 0
        with open(const.RESULT_FILE, "r") as f:
            r = f.read()
            if r:
                result = int(r)
        return result

    def set_highest_score(self):
        """
        set the highest score to the result file
        """
        h_s = self.get_highest_score()
        if self.score > h_s:
            with open(const.RESULT_FILE, 'w') as f:
                f.write("{0}".format(self.score))


