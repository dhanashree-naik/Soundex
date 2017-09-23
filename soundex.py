from fst import FST
import string, sys
from fsmutils import composechars, trace


def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    
    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('1')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.add_state('7')
    f1.add_state('8')
    f1.add_state('9')
    f1.initial_state = '1'

    # Set all the final states
    
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')
    f1.set_final('7')
    f1.set_final('8')
    f1.set_final('9')
    f1.set_final('3')
    
    # Add the rest of the arcs
    for letter in string.ascii_letters:
        f1.add_arc('1', '3', (letter), (letter))
        #f1.add_arc('2', '3', ['a','e','i','o','u','w','y'], ())
        
        if letter in 'aeiouhwyAEIOUHWY':
            f1.add_arc('1','3',(letter), (letter))
            f1.add_arc('3', '3', (letter), ())
           
            f1.add_arc('4','3',(letter),())
            f1.add_arc('5','3',(letter),() )
            f1.add_arc('6','3',(letter),() )
            f1.add_arc('7','3',(letter),() )
            f1.add_arc('8','3',(letter),())
            f1.add_arc('9','3',(letter),() )  
        
            
        elif letter in 'bfpvBFPV':
            f1.add_arc('1', '4', (letter), (letter))
            f1.add_arc('3', '4', (letter), ('1'))
            f1.add_arc('4','4',(letter),() )
            f1.add_arc('5','4',(letter),('1') )
            f1.add_arc('6','4',(letter),('1') )
            f1.add_arc('7','4',(letter),('1') )
            f1.add_arc('8','4',(letter),('1') )
            f1.add_arc('9','4',(letter),('1') )


        elif letter in 'cgjkqsxzCGJKQSXZ':
            f1.add_arc('1', '5', (letter), (letter))
            f1.add_arc('3', '5', (letter), ('2'))
            f1.add_arc('5','5',(letter),())
            f1.add_arc('4', '5', (letter), ('2'))
            f1.add_arc('6', '5', (letter), ('2'))
            f1.add_arc('7', '5', (letter), ('2'))
            f1.add_arc('8', '5', (letter), ('2'))
            f1.add_arc('9', '5', (letter), ('2'))
         
        
        elif letter in 'dtDT':
            f1.add_arc('1', '6', (letter), (letter))
            f1.add_arc('3', '6', (letter), ('3'))
            f1.add_arc('6','6',(letter),() )
            
            f1.add_arc('4', '6', (letter), ('3'))
            f1.add_arc('5', '6', (letter), ('3'))
            f1.add_arc('9', '6', (letter), ('3'))
            f1.add_arc('7', '6', (letter), ('3'))
            f1.add_arc('8', '6', (letter), ('3'))

        elif letter in 'lL':
            f1.add_arc('1', '7', (letter), (letter))
            f1.add_arc('3', '7', (letter), ('4'))
            f1.add_arc('7','7',(letter),() )
           
            f1.add_arc('4', '7', (letter), ('4'))
            f1.add_arc('5', '7', (letter), ('4'))
            f1.add_arc('6', '7', (letter), ('4'))
            f1.add_arc('8', '7', (letter), ('4'))
            f1.add_arc('9', '7', (letter), ('4'))

        elif letter in 'mnMN':
            f1.add_arc('1', '8', (letter), (letter))
            f1.add_arc('3', '8', (letter), ('5'))
            f1.add_arc('8','8',(letter),() )
            
            f1.add_arc('4', '8', (letter), ('5'))
            f1.add_arc('5', '8', (letter), ('5'))
            f1.add_arc('6', '8', (letter), ('5'))
            f1.add_arc('7', '8', (letter), ('5'))
            f1.add_arc('9', '8', (letter), ('5'))

        
        elif letter in 'rR':
            f1.add_arc('1', '9', (letter), (letter))
            f1.add_arc('3', '9', (letter), ('6'))
            f1.add_arc('9','9',(letter),() )
       
            f1.add_arc('5', '9', (letter), ('6'))
            f1.add_arc('4', '9', (letter), ('6'))
            f1.add_arc('6', '9', (letter), ('6'))
            f1.add_arc('7', '9', (letter), ('6'))
            f1.add_arc('8', '9', (letter), ('6'))
        
    
    
    

    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    
    f2.initial_state = '1'
    f2.set_final('4')
    f2.set_final('3')
    f2.set_final('2')
    f2.set_final('1')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))

    for n in range(10):
        f2.add_arc('1', '2', (str(n)), (str(n)))
        f2.add_arc('2', '3', (str(n)), (str(n)))
        f2.add_arc('3', '4', (str(n)), (str(n)))
        f2.add_arc('4', '4', (str(n)), ())
        

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('2')
    f3.add_state('3')
    f3.add_state('4')
  
   
    
    f3.initial_state = '1'
    
    f3.set_final('4')

    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))    
    
    f3.add_arc('1', '2', (), ('0'))
    f3.add_arc('2', '3', (), ('0'))
    f3.add_arc('3', '4', (), ('0'))
    

        
    for number in xrange(10):
        f3.add_arc('1', '2', (str(number)), (str(number)))
        f3.add_arc('2', '3', (str(number)), (str(number)))
        f3.add_arc('3', '4', (str(number)), (str(number)))
    
    
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2,f3)))
        #print("%s -> %s" % (user_input, f3.transduce(user_input)))
        #print("%s -> %s" % (user_input, trace(f1,user_input)))
