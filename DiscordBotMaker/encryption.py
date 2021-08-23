import pickle


class Encoder:
    def __init__(self, characterList):
        self.characterList = characterList

        if type(self.characterList) is list:
            pass
        else:
            raise TypeError("CharacterList must be a list!")

    def encode(self, input):
        """ Encode given text

        Arguments:
            input: Text to encode
        Returns:
            Encoded number
        """

        output = ""
        for char in input:
            nChar = self.characterList.index(char)
            output = output+str(nChar)+"|"
    
        return output

    def triple_encode(self, input):
        """ Triple-encode given text

        Arguments:
            input: Text to encode
        Returns:
            Encoded number
        """

        output = self.encode(input)
        output = self.encode(output)
        output = self.encode(output)

        return output

    def ultra_encode(self, input):
        """ Ultra-encode given text

        Arguments:
            input: Text to encode
        Returns:
            Encoded number
        """

        output = self.encode(input)
        output = self.encode(output)
        output = self.encode(output)
        output = self.encode(output)
        output = self.encode(output)
        output = self.encode(output)
        output = self.encode(output)
        output = self.encode(output)

        return output


class Decoder:
    def __init__(self, characterList):
        self.characterList = characterList

        if type(self.characterList) is list:
            pass
        else:
            raise TypeError("CharacterList must be a list!")

    def ultra_decode(self, input):
        """ Ultra-decode given text

        Arguments:
            input: Text to decode
        Returns:
            Decoded number
        """

        output = self.decode(input)
        output = self.decode(output)
        output = self.decode(output)
        output = self.decode(output)
        output = self.decode(output)
        output = self.decode(output)
        output = self.decode(output)
        output = self.decode(output)

        return output

    def decode(self, input):
        """ Decode encoded text

        Arguments:
            input: Text to decode
        Returns:
            Decoded number
        """

        output = ""
        for char in input.split("|")[:-1]:
            nChar = self.characterList[int(char)]
            output = output+str(nChar)
    
        return output

    def decode_triple(self, input):
        """ Decode triple-encoded text

        Arguments:
            input: Text to decode
        Returns:
            Decoded number
        """

        output = self.decode(input)
        output = self.decode(output)
        output = self.decode(output)

        return output
