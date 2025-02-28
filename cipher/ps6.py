import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower = {}
        lower = lower.fromkeys(list(string.ascii_lowercase))
        upper = {}
        upper = upper.fromkeys(list(string.ascii_uppercase))
        if shift < 0 or shift > 26:
            raise ValueError('The shift value is out of boundaries!')
        else:
            for entry in lower:
                lower[entry] = chr((((ord(entry) - 97)+shift)%26)+97)
            for entry in upper:
                upper[entry] = chr((((ord(entry) - 65)+shift)%26)+65)
            CipherDict = dict(**upper, **lower)
        return CipherDict.copy()               

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        text = self.get_message_text()
        text = list(text)
        CipherDict = self.build_shift_dict(shift)
        PunctuationChar = list(string.punctuation)+ list(' ') + list(string.digits)
        messageShifted = []
        if shift < 0 or shift > 26:
            raise ValueError('The shift value is out of boundaries!')
        else:
            for letter in text:
                if letter in PunctuationChar:
                    messageShifted.append(letter)
                else:
                    messageShifted.append(CipherDict[letter])
        messageShifted = ''.join(messageShifted)
        return messageShifted

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self,text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted[:]

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        text = self.get_message_text()
        self.__init__(text, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def is_validword(self, word):
        '''
        Determines if word is a valid word, ignoring
        capitalization and punctuation
        
        word_list (list): list of words in the dictionary.
        word (string): a possible word.
        
        Returns: True if word is in word_list, False otherwise
        
        Example:
        >>> is_word(word_list, 'bat') returns
        True
        >>> is_word(word_list, 'asdf') returns
        False
        '''
        validwords = self.get_valid_words()
        word = word.lower()
        word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        return word in validwords


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        register = []
        iterations = 0
        while iterations <= 26:
            wordsMatched = 0 
            plaintext = self.apply_shift(26 - iterations)
            text = plaintext.split(' ')
            for word in text:
                if self.is_validword(word):
                    wordsMatched += 1
            register.append(wordsMatched)
            if wordsMatched == len(text):
                break
            iterations += 1
        if register.index(max(register)) == 0:
            shiftValue = 0
        else:
            shiftValue = 26 - register.index(max(register))
        decryptMessage = self.apply_shift(shiftValue)
        return shiftValue, decryptMessage

def decrypt_story():
    EncryptedStory = CiphertextMessage(get_story_string())
    DecryptedStory = EncryptedStory.decrypt_message()
    return DecryptedStory

##Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('Message is Nonsense words: meanwhile old zero that universe reduction sometime pick hurrah sock everything serve should stomach hesitate', 2)
#print('Expected Output: Oguucig ku Pqpugpug yqtfu: ogcpyjkng qnf bgtq vjcv wpkxgtug tgfwevkqp uqogvkog rkem jwttcj uqem gxgtavjkpi ugtxg ujqwnf uvqocej jgukvcvg')
#print('Actual Output:', plaintext.get_message_text_encrypted())
#    
##Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage('Oguucig ku Pqpugpug yqtfu: ogcpyjkng qnf bgtq vjcv wpkxgtug tgfwevkqp uqogvkog rkem jwttcj uqem gxgtavjkpi ugtxg ujqwnf uvqocej jgukvcvg')
#print('Expected Output:', (2, 'Message is Nonsense words: meanwhile old zero that universe reduction sometime pick hurrah sock everything serve should stomach hesitate'))
#print('Actual Output:', ciphertext.decrypt_message())
#
##Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('Message is Nonsense words: could alone dish breakfast tax', 24)
#print('Expected Output: Kcqqyec gq Lmlqclqc umpbq: amsjb yjmlc bgqf zpcyidyqr ryv')
#print('Actual Output:', plaintext.get_message_text_encrypted())
#    
##Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage('Kcqqyec gq Lmlqclqc umpbq: amsjb yjmlc bgqf zpcyidyqr ryv')
#print('Expected Output:', (24, 'Message is Nonsense words: could alone dish breakfast tax'))
#print('Actual Output:', ciphertext.decrypt_message())
