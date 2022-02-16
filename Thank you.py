class ByeBye:
    def __init__(self , ne , word):
        self.ne = ne
        self.word = word

    def hi(self):
        print(f"Thank you {self.ne}")
    def bye(self):
        print(f"Do take care of {self.word}")

    @staticmethod
    def greet():
        print("I hope you will have a nice day ahead :)")

Itr = ByeBye("Everyone" , "yourself")
Itr.hi()
Itr.bye()
Itr.greet()