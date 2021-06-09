#  create class name Duck
class Duck:
    #  create two variable sound and walking
    sound = 'quaaaaaaack'
    walking = 'walks like a duck. '
    # create function for self (using self for print all the thing in variable
    def quack(self):
        print(self.sound)
    def walk(self):
         print(self.walking)
# create another function name main with one black argument
def main():
    #  here we have put all the data in this function create new variable (donald) and say donald is == Duck

    donald = Duck()

    donald.quack()
    donald.walk()

if __name__=='__main__': main()
