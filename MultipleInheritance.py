class Father():
   def skills(self):
       print("gardening,programming")

class Mother():
   def skills(self):
       print("cooking,art")

   def more_skills(self):
       print("driving")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()
c.more_skills()