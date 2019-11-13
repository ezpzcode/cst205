class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
        self.b = 'aha'

    def greeting(self):
    	print(self.hello)

    def bb(self):
    	print(self.b)

james = Person()
a = Person()
james.greeting()
a.bb()
