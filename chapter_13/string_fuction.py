
class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n} '
    def __str__(self):
        return f'srt: the number of bunnies is {self._n}'



x = bunny (78)
print(ascii(x))