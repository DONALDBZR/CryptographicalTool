# Importing System
import sys
# Importing command
from click import command
# Importing Numerical Python
import numpy
# Importing Euclidean
import Euclidean
# Importing Mathematics
import math
# Cryptographical Tool class
class CryptographicalTool:
    # Constructor method
    def __init__(self):
        # Class variables
        self.text: str
        self.result: str
        self.NumericalPython = numpy
        self.Euclidean = Euclidean
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Mathematics = math
        # Calling the menu
        self.menu()
    # Text accessor method
    def getText(self):
        return self.text
    # Text mutator method
    def setText(self, text: str):
        self.text = text
    # Result accessor method
    def getResult(self):
        return self.result
    # Result mutator method
    def setResult(self, result: str):
        self.result = result
    # Error handler method
    def handleError(self, errorNumber):
        # If-statement to determine the kind of error
        if errorNumber == 1:
            sys.exit("Incorrect key was pressed!")
        elif errorNumber == 2:
            sys.exit("Error on the Hill Cipher's encryption!")
        elif errorNumber == 3:
            sys.exit("Error on the Caesar Cipher")
    # Menu method
    def menu(self):
        print("========================================")
        print("Press 0 to close")
        print("Press 1 for Caesar Cipher")
        print("Press 2 for Hill Cipher")
        print("Press 3 for Vinegère Cipher")
        print("Press 4 for Route Cipher")
        self.selector()
    # Selector method
    def selector(self):
        # Local variables
        choice = int(input("Enter the value: "))
        print("========================================")
        # If-statement to select the correct exercise
        if choice == 0:
            sys.exit("Closing the program")
        elif choice == 1:
            self.handleError(3)
        elif choice == 2:
            self.handleError(2)
        elif choice == 3:
            self.vinegereCipher()
        elif choice == 4:
            self.routeCipher()
        else:
            self.handleError(1)
    # Caesar Cipher method
    def caesarCipher(self):
        print("========================================")
        self.setText(str(input("Enter the text to be crypted: ")))
        self.setShift(int(input("Enter the shifted amount: ")))
        print("========================================")
        print("Press 0 to cancel cipher")
        print("Press 1 to encrypt")
        print("Press 2 to decrypt")
        print("========================================")
        choice = int(input("Enter the value: "))
        print("========================================")
        # Caesar Cipher Encryption function
        def caesarCipherEncryption(text, shift):
            # Local variables
            result = ""
            # For-loop for traversing the text
            for index in range(0, len(text), 1):
                # Local variables
                character = text[index]
                # If-statement to verify whether the text is in uppercase
                if character.isupper():
                    result = result + chr((ord(character) + shift - 65) % 26 + 65)
                else:
                    result = result + chr((ord(character) + shift - 97) % 26 + 97)
            print("Input: " + text + "\nShift: " + str(shift) + "\nOutput: " + result)
        # Caesar Cipher Decryption function
        def caesarCipherDecryption(text, shift):
            # Local variables
            result = ""
            # For-loop for traversing the text
            for index in range(0, len(text), 1):
                # Local variables
                character = text[index]
                # If-statement to verify whether the text is in uppercase
                if character.isupper():
                    result = result + chr((ord(character) - shift - 65) % 26 + 65)
                else:
                    result = result + chr((ord(character) - shift - 97) % 26 + 97)
            print("Input: " + text + "\nShift: " + str(shift) + "\nOutput: " + result)
        # If-statement to make the selection
        if choice == 0:
            self.menu()
        elif choice == 1:
            caesarCipherEncryption(self.getText(), self.getShift())
            self.menu()
        elif choice == 2:
            caesarCipherDecryption(self.getText(), self.getShift())
            self.menu()
        else:
            self.handleError(1)
    # Hill Cipher method
    def hillCipher(self):
        self.setText(str(input("Enter the text to encrypt/decrypt: ")).upper())
        print("========================================")
        print("Press 0 to cancel cipher")
        print("Press 1 to encrypt")
        print("Press 2 to decrypt")
        print("========================================")
        choice = int(input("Enter the value: "))
        print("========================================")
        # Matrix Modulus Inverse function
        def matrixModulusInverse(matrix, modulus):
            # Finding the determinant
            determinant = int(self.numericalPython.round(self.numericalPython.linalg.det(matrix)))
            # Finding the determinant in a specific modulus
            determinantInverse = command= lambda: self.euclidean.extendedGreatestCommonDivisor(determinant, modulus)[1] % modulus
            # Multiplying the Determinant Inverse to the product of the determinant and the inverted Matrix
            matrixModulusInverse = (determinantInverse * self.numericalPython.round(determinant * self.numericalPython.linalg.inv(matrix)).astype(int) % modulus)
            return matrixModulusInverse
        # Encode function
        def encode(message, key):
            encrypted = ""
            messageInNumbers = []
            # For-loop to convert message into numbers
            for firstIndex in range(0, len(message), 1):
                for secondIndex in range(0, len(self.letters), 1):
                    # If-statement to verify that the letter in the message is the same as in the array
                    if message[firstIndex] == self.letters[secondIndex]:
                        messageInNumbers.append(secondIndex + 1)
            splitPlainText = [
                messageInNumbers[index : index + int(key.shape[0])]
                for index in range(0, len(messageInNumbers), int(key.shape[0]))
            ]
            # For-loop for transposing the plain text
            for plainText in splitPlainText:
                plainText = self.numericalPython.transpose(self.numericalPython.asarray(plainText))[:, self.numericalPython.newaxis]
                numbers = self.numericalPython.dot(key, plainText) % len(self.letters)
                figure = numbers.shape[0]
                # For-loop to add the cipher text
                for firstIndex in range(figure):
                    number = int(numbers[firstIndex, 0])
                    for secondIndex in range(0, len(self.letter), 1):
                        # If-statement to verify that the integers are equal
                        if number - 1 == secondIndex:
                            encrypted += self.letters[secondIndex]
                        else:
                            self.handleError(2)
            return encrypted
        # Hill Cipher Encrypt function
        def hillCipherEncrypt(message):
            key = self.numericalPython.matrix([[3, 3], [2, 5]])
            keyInverse = matrixModulusInverse(key, len(self.letters))
            cipherText = encode(message, key)
            print("Plaint Text: " + message + "\nCipher Text: " + cipherText)
        # Decode function
        def decode(cipher, keyInverse):
            decrypted = ""
            cipherInNumbers = []
            # For-loop to convert the cipher into number
            for firstIndex in range(0, len(cipher), 1):
                for secondIndex in range(0, len(self.letters), 1):
                    # If-statement to verify that the letter in the message is the same as in the array
                    if cipher[firstIndex] == self.letters[secondIndex]:
                        cipherInNumbers.append(secondIndex + 1)
            splitCipher = [
                cipherInNumbers[index : index + int(keyInverse.shape[0])]
                for index in range(0, len(cipherInNumbers), int(keyInverse.shape[0]))
            ]
            # For-loop for transposing the cipher
            for cipher in splitCipher:
                cipher = self.numericalPython.transpose(self.numericalPython.asarray(cipher))[:, self.numericalPython.newaxis]
                numbers = self.numericalPython.dot(keyInverse, cipher) % len(self.letters)
                figures = numbers.shape[0]
                # For-loop to add the plain text
                for firstIndex in range(figures):
                    number = int(numbers[firstIndex, 0])
                    for secondIndex in range(0, len(self.letters), 1):
                        # If-statement to verify that the integers are equal
                        if number - 1 == secondIndex:
                            encrypted += self.letters[secondIndex]
                        else:
                            self.handleError(2)
            return decrypted
        # Hill Cipher Decrypt function
        def hillCipherDecrypt(message):
            key = self.numericalPython.matrix([[3, 3], [2, 5]])
            keyInverse = matrixModulusInverse(key, len(self.letters))
            plainText = decode(message, keyInverse)
            print("Cipher Text: " + message + "\nPlain Text: " + plainText)
        # If-statement to make the selection
        if choice == 0:
            self.menu()
        elif choice == 1:
            hillCipherEncrypt(self.getText())
            self.menu()
        elif choice == 2:
            hillCipherDecrypt(self.getText())
            self.menu()
        else:
            self.handleError(1)
        self.menu()
    # Vinegère Cipher method
    def vinegereCipher(self):
        # Local variables
        string = str(input("Enter the string to be encrypted: "))
        keyword = str(input("Enter the keyword: "))
        print("Press 0 to return back to the menu")
        print("Press 1 to encrypt")
        print("Press 2 to decrypt")
        choice = int(input("Enter a value: "))
        print("========================================")
        # Generate Key function
        def generateKey(string, key):
            key = list(key)
            # If-statement to verify whether the length of the string and the key are equal
            if len(string) == len(key):
                return key
            else:
                # For-loop to generate the key
                for index in range(len(string) - len(key)):
                    key.append(key[index % len(key)])
            return("" . join(key))
        # Cipher Text function
        def cipherText(string, key):
            # Local variables
            text = []
            # For-loop to return the encrypted text
            for index in range(len(string)):
                data = (ord(string[index]) + ord(key[index])) % 26
                data += ord('A')
                text.append(chr(data))
            return("" . join(text))
        # Original Text function
        def originalText(cipher_text, key):
            # Local variables
            text = []
            # For-loop to decrypt the cipher
            for index in range(len(cipher_text)):
                data = (ord(cipher_text[index]) - ord(key[index]) + 26) % 26
                data += ord('A')
                text.append(chr(data))
            return("" . join(text))
        # If-statement to verify whether to encrypt or decrypt the data entered
        if choice == 0:
            self.menu()
        elif choice == 1: 
            key = generateKey(string, keyword)
            self.setResult(cipherText(string, key))
            origin = originalText(self.getResult(), key)
            print("Original Text: " + string + "\nEncrypted/Decrypted: " + self.getResult())
        elif choice == 2:
            key = generateKey(string, keyword)
            self.setResult(originalText(string, key))
            print("Original Text: " + string + "\nEncrypted/Decrypted: " + self.getResult())
        # CryptographicalTool.menu()
        self.menu()
    # Route Cipher method
    def routeCipher(self):
        self.setText(str(input("Enter the text to encrypt/decrypt: ")))
        print("========================================")
        print("Press 0 to cancel cipher")
        print("Press 1 to encrypt")
        print("Press 2 to decrypt")
        print("========================================")
        choice = int(input("Enter the value: "))
        print("========================================")
        # Encrypt function
        def encrypt(plainText: str):
            # Local variables
            index = 0
            matrixRepresentation = []
            cipherText: str
            stepSize = int(input("Enter the step's size: "))
            # For-loop for creating a matrix from the plain text with the step's size as width
            for firstIndex in range(0, self.Mathematics.ceil(len(plainText) / stepSize), 1):
                matrixRow = []
                for secondIndex in range(0, stepSize, 1):
                    if firstIndex * stepSize + secondIndex < len(plainText):
                        matrixRow.append(plainText[firstIndex * stepSize + secondIndex])
                    else:
                        matrixRow.append("-")
                matrixRepresentation.append(matrixRow)
            matrixWidth = len(matrixRepresentation[0])
            matrixHeight = len(matrixRepresentation)
            # If-statement to verify that the matrix's width is less than the matrix's height
            if matrixWidth < matrixHeight:
                allowedDepth = matrixWidth // 2
            else:
                allowedDepth = matrixHeight // 2
            # For-loop to encrypt the plain text by going in a spiral form by starting in the top-right corner
            for firstIndex in range(0, allowedDepth, 1):
                for secondIndex in range(firstIndex, matrixHeight - firstIndex - 1, 1):
                    cipherText += matrixRepresentation[secondIndex][matrixWidth - firstIndex - 1]
                for secondIndex in range(matrixWidth - firstIndex - 1, firstIndex, -1):
                    cipherText += matrixRepresentation[matrixHeight - firstIndex - 1][secondIndex]
                for secondIndex in range(matrixHeight - firstIndex - 1, firstIndex, -1):
                    cipherText += matrixRepresentation[secondIndex][firstIndex]
                for secondIndex in range(firstIndex, matrixWidth - firstIndex - 1, 1):
                    cipherText += matrixRepresentation[firstIndex][secondIndex]
            return cipherText
        # Decrypt function
        def decrypt(cipherText: str):
            # Local variables
            stepSize = int(input("Enter the step's size: "))
            index = 0
            plainText: str
            matrixWidth = stepSize
            matrixHeight = self.Mathematics.ceil(len(cipherText) / stepSize)
            plainTextMatrix = [[0 for firstIndex in range(0, matrixWidth, 1)] for secondIndex in range(0, matrixHeight, 1)]
            # If-statement to verify that the matrix's width is less than the matrix's height
            if matrixWidth < matrixHeight:
                allowedDepth = matrixWidth // 2
            else:
                allowedDepth = matrixHeight // 2
            # For-loop to decrypt the cipher text
            for firstIndex in range(0, allowedDepth, 1):
                for secondIndex in range(firstIndex, matrixHeight - firstIndex - 1, 1):
                    plainTextMatrix[secondIndex][matrixWidth - firstIndex - 1] = cipherText[index]
                    index += 1
                for secondIndex in range(matrixWidth - firstIndex - 1, firstIndex, -1):
                    plainTextMatrix[matrixHeight - firstIndex - 1][secondIndex] = cipherText[index]
                    index += 1
                for secondIndex in range(matrixHeight - firstIndex - 1, firstIndex, -1):
                    plainTextMatrix[secondIndex][firstIndex] = cipherText[index]
                    index += 1
                for secondIndex in range(firstIndex, matrixWidth - firstIndex - 1, 1):
                    plainTextMatrix[firstIndex][secondIndex] = cipherText[index]
                    index += 1
            # For-Loop for reconstructing the plain text
            for firstIndex in range(0, matrixHeight, 1):
                for secondIndex in range(0, matrixWidth, 1):
                    plainText += plainText[firstIndex][secondIndex]
            return plainText
        # If-statement to verify whether to encrypt or decrypt the data entered
        if choice == 0:
            self.menu()
        elif choice == 1: 
            self.setResult(encrypt(self.getText()))
            print("Plain Text: " + self.getText() + "\nCipher Text: " + self.getResult())
            self.menu()
        elif choice == 2:
            self.setResult(decrypt(self.getText()))
            print("Cipher Text: " + self.getText() + "\nPlain Text: " + self.getResult())
            self.menu()
# Euclidean class
class Euclidean:
    # Constructor method
    def __init__(self):
        pass
    # Greatest Common Divisor method
    def greatestCommonDivisor(self, firstNumber: int, secondNumber: int):
        # If-statement to verify that the first number is zero
        if firstNumber == 0:
            return secondNumber
        else:
            return self.greatestCommonDivisor(secondNumber % firstNumber, firstNumber)
    # Extended Greatest Common Divisor method
    def extendedGreatestCommonDivisor(self, firstNumber: int, secondNumber: int):
        # If-statement to verify that the first number is zero
        if firstNumber == 0:
            return secondNumber, 0, 1
        else:
            greatestCommonDivisor, firstIdentity, secondIdentity = self.extendedGreatestCommonDivisor(secondNumber % firstNumber, firstNumber)
            return (greatestCommonDivisor, firstIdentity - (secondNumber // firstNumber) * secondIdentity, secondIdentity)
# Instantiating Cryptographical Tool
Test = CryptographicalTool()