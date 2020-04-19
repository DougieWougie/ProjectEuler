thousands = {
    '0': '', 
    '1': 'one thousand ',
    '2': 'two thousand ',
    '3': 'three thousand ',
    '4': 'four thousand ',
    '5': 'five thousand ',
    '6': 'six thousand ',
    '7': 'seven thousand ',
    '8': 'eight thousand ',
    '9': 'nine thousand ',
    }
hundreds = {
    '0': '',
    '1': 'one hundred ',
    '2': 'two hundred ',
    '3': 'three hundred ',
    '4': 'four hundred ',
    '5': 'five hundred ',
    '6': 'six hundred ',
    '7': 'seven hundred ',
    '8': 'eight hundred ',
    '9': 'nine hundred ',
    }
units = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    }
tens = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    }
twenties = {
    '0': '',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
    }

total = 0

for i in range(1, 1001):
    sentance = ''
    numberString = str(i)

    if len(numberString) == 4:
        sentance = thousands[numberString[0]] + hundreds[numberString[1]]
        if not numberString[1:4] == '000':
            sentance = sentance + 'and '
        if numberString[2] == '1':
            sentance = sentance + tens[numberString[2]+numberString[3]]
        else:
            sentance = sentance + twenties[numberString[2]] + units[numberString[3]]

    if len(numberString) == 3:
        sentance = hundreds[numberString[0]]
        if not numberString[1:3] == '00':
            sentance = sentance + 'and '
        if numberString[1] == '1':
            sentance = sentance + tens[numberString[1]+numberString[2]]
        else:
            sentance = sentance + twenties[numberString[1]] + units[numberString[2]]

    if len(numberString) == 2:
        if numberString[0] == '1':
            sentance = tens[numberString]
        else:
            sentance = twenties[numberString[0]] + units[numberString[1]]

    if len(numberString) == 1:
        sentance = units[numberString[0]]

    total = total + len(sentance.replace(' ',''))
    print(sentance + str(total) + '\n')
