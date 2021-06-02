class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self.type = kwargs['type']
        if 'name' in kwargs: self.name = kwargs['name']
        if 'sound' in kwargs: self.sound = kwargs['sound']

    def type(self,t = None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def type(self,n = None):
        if n: self.name = n
        try: return self._name
        except AttributeError: return None

    def __str__(self):
        return f'The {self.type} is named "{self.name}" and says "{self.sound}".'

class Duck(Animal):
    def __init__(self, **kwargs):
        self.type = 'Duck'
        if type  in kwargs: del kwargs['type']
        super().__init__(**kwargs)



class kitten(Animal):
    def __init__(self, **kwargs):
        self.type = 'kitten'
        if type  in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name} will now kill all {s}!')


def main():
        a0 = kitten(name = 'fluffy', sound='rwar')
        a1 = Duck(name='Donald', sound='quack')
        print(a1)
        print(a0)
        a0.kill('humans')



class RevStr(str):
    def __str__(self):
        return self[::-1]
    def main2():
        print('hello')
if __name__ == '__main__':
     main()




