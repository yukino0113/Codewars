#https://www.codewars.com/kata/568018a64f35f0c613000054/train/python

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if not self.lives:
            raise Exception("Omae wa mo shindeiru")

        if n == self.number:
            return True
        else:
            self.lives -= 1
            return False