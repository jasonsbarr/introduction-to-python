# Exercise: genPrimes
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

# Exercise: hand
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 14 minutes

# In this problem, you'll be asked to read through an object-oriented implementation of the hand from the word game problem of Problem
# Set 4. You'll then be asked to implement one of its methods. Note that the implementation of the object-oriented version of the hand
# is a bit different than how we did things with the functional implementation; pay close attention to doc strings and read through the
# implementation carefully.

# To begin: Download hand.py and read through the file. Be sure to understand what's going on in the file. Make a few instances of the
# Hand class, and play around with the existing methods.

# When you have completed reading through the file, implement the update method.

# Paste the entire Hand class in the box below.

# The __str__ method is this:

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output
        
# A more concise version of this code might be

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        for letter in sorted(self.hand.keys()):
            output += letter * self.hand[letter]
        return output
        
# Use whichever __str__ method you like. This will make sure the grading of the hand's display is consistent.
