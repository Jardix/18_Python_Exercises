def print_upper_words(words):
    """Notes: This does 'not' print each word seperately, it prints each 'letter' seperately, even after referring to the solution.
        
        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        P
        R
        O
        G
        R
        A
        M
        M
        I
        N
        G

        I
        S

        P
        R
        E
        T
        T
        Y

        F
        U
        N    
     """
    for counter in words:
        print(counter.upper())

def print_upper_words2(words):
    """Notes: This should take a list of words and print out only the ones that start with e, capitolized. 
        >>> def print_upper_words2("Echo", "Bat", "Earring", "Dangle")
        ECHO
        EARRING
      """
    
    for counter in words:
        if counter.startswith("e") or counter.startswith("E"):
            print(counter.upper())



def print_upper_words3(words, must_start_with):
    """Notes: This function should take a set [] of strings and return only the strings that have the specified letter(s) in uppercase. 
        >>> def print_upper_words3(words, must_start_with):
            def print_upper_words3(["Hello", "Goodbye", "Yankee"], must_start_with={"h", "y"}):
                returns
                    "HELLO"
                    "YANKEE"            
    """
    # My version:
    # Not sure how to select only the first or second key/value in this 'object', if that's what it is. 
    # for counter in words:
    #     if counter.startswith(f"{must_start_with}"):
    #         print(counter.upper())
    # Solution: 
    # I actually had a structure like this for the second one! I see that the 'object' {} is iterable; that makes sense now. 
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

