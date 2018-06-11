class Parent(object):

    def override(self):
        print("PArent override()")

    def implicit(self):
        print("parent impllicit()")

    def altered(self):
        print("parent altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("child, before parent altered()")
        super(Child, self).altered()
        print("CHILD, after parent altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
