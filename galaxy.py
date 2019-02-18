class Galaxy:
   """ learning accessors and mutators """

   # initializer ("constructor") method -------------------------------
   def __init__(self):

      # class-defined instance attributes (attributes)
      self.name = "undefined"
      self.magnitude = 0.0

   # mutator ("set") methods -------------------------------
   def set_magnitude(self, the_mg):
      if (the_mg < -3 or the_mg > 30):
         return False
      # else
      self.magnitude = the_mg
      return True

   def set_name(self, the_nm):
      if (type(the_nm) != str or len(the_nm) > 30):
         return False
      # else
      self.name = the_nm
      return True

   # accessor ("get") methods -------------------------------
   def get_magnitude(self):
      return self.magnitude

   def get_name(self):
      return self.name

# client --------------------------------------------

# instantiate two Galaxy objects in main
gal1 = Galaxy()
gal2 = Galaxy()

# show both gal1 and gal2 before mutators
print( "INITIAL (objects):\n")
print( "\tgal1's name is \"{}\" and has magnitude {}.".
       format(gal1.get_name(), gal1.get_magnitude()) )
print( "\tgal2's name is \"{}\" and has magnitude {}.".
       format(gal2.get_name(), gal2.get_magnitude()) )

# try to set some data
gal1.set_name("X")
gal1.set_magnitude(100)
gal2.set_name("Stephan's Third")
gal2.set_magnitude(13.2)

# let's see what happened
print( "\nAfter mutation:\n")
print( "\tgal1's name is \"{}\" and has magnitude {}.".
       format(gal1.get_name(), gal1.get_magnitude()) )
print( "\tgal2's name is \"{}\" and has magnitude {}.".
       format(gal2.get_name(), gal2.get_magnitude()) )

""" --------------------------- RUN -------------------------

INITIAL (objects):

	gal1's name is "undefined" and has magnitude 0.0.
	gal2's name is "undefined" and has magnitude 0.0.

After mutation:

	gal1's name is "X" and has magnitude 0.0.
	gal2's name is "Stephan's Third" and has magnitude 13.2.

--------------------------- END RUN  ------------------------- """
