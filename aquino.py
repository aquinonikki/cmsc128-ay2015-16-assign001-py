#!/usr/bin/python

#sub-function for numToWord
def count(num2):
	if(int(num2) == 1):
		return "one"
	elif((int(num2)) == 2):
		return "two"
	elif((int(num2)) == 3):
		return "three"
	elif((int(num2)) == 4):
		return "four"
	elif((int(num2)) == 5):
		return "five"
	elif((int(num2)) == 6):
		return "six"
	elif((int(num2)) == 7):
		return "seven"
	elif((int(num2)) == 8):
		return "eight"
	elif((int(num2)) == 9):
		return "nine"
	elif((int(num2)) == 0):
		return "zero"

#sub-function for numToWord
def count2(number): 
	if(int(number) == 2):
		return "twenty "
	elif(int(number) == 3):
		return "thirty "
	elif(int(number) == 4):
		return "forty "
	elif(int(number) == 5):
		return "fifty "
	elif(int(number) == 6):
		return "sixty "
	elif(int(number) == 7):
		return "seventy "
	elif(int(number) == 8):
		return "eighty "
	elif(int(number) == 9):
		return "ninety "
		
#sub-function for numToWord
def count3(number):
	if(int(number) == 1):
		return "eleven "
	elif(int(number) == 2):
		return "twelve "
	elif(int(number) == 3):
		return "thirteen "
	elif(int(number) == 4):
		return "fourteen "
	elif(int(number) == 5):
		return "fifteen "
	elif(int(number) == 6):
		return "sixteen "
	elif(int(number) == 7):
		return "seventeen "
	elif(int(number) == 8):
		return "eighteen "
	elif(int(number) == 9):
		return "nineteen "
	elif(int(number) == 0):
		return "ten "

#numToWord
def numToWords(num):
	print "Number to Words"
	#num = raw_input(" Enter a number: ")
	word = " "

	while (num != 0):
		num1 = len(str(num))
		if(int(num1) == 7):
			num3 = (int(num) % 1000000)
			num2 = ((int(num) - int(num3))/1000000)
			if((int(num2)) != 0):
				word = str(count(num2 = num2)) + " million "
			num = int(num3)
		elif(int(num1) == 6): 
			num3 = (int(num) % 100000)
			num2 = ((int(num) - int(num3))/100000)
			if((int(num2)) != 0):
				word = str(word) + str(count(num2 = num2)) + " hundred "
			num = int(num3)
		elif(int(num1) == 5):
			num3 = (int(num) % 10000)
			num2 = ((int(num) - int(num3))/10000)
			num4 = int(num3) / 1000
			if(int(num2) != 1):
				word = str(word) + count2(number = num2)
				num = int(num3)
			else:
				word = str(word) + count3(number = num3) + " thousand "
				num = int(num3) - (num4*1000)
		elif(int(num1) == 4):
			num3 = (int(num) % 1000)
			num2 = ((int(num) - int(num3))/1000)
			if((int(num2)) != 0):
				word = str(word) + str(count(num2 = num2)) + " thousand "
			num = int(num3)
		elif(int(num1) == 3): 
			num3 = (int(num) % 100)
			num2 = ((int(num) - int(num3))/100)
			if((int(num2)) != 0):
				word = str(word) + str(count(num2 = num2)) + " hundred "
			num = int(num3)
		elif(int(num1) == 2):
			num3 = (int(num) % 10)
			num2 = ((int(num) - int(num3))/10)
			if(int(num2) != 1):
				word = str(word) + count2(number = num2)
				num = int(num3)
			else:
				word = str(word) + count3(number = num3)
				num = 0
		elif (int(num1) == 1):
			word = str(word) + str(count(num2 = num))
			num = 0
		else:
			print "Invalid input!"
			num = 0
	
	print word
	
def ones(o):
	if(str(o) == "one"):
		return "1"
	elif(str(o) == "two"):
		return "2"
	elif(str(o) == "three"):
		return "3"
	elif(str(o) == "four"):
		return "4"
	elif(str(o) == "five"):
		return "5"
	elif(str(o) == "six"):
		return "6"
	elif(str(o) == "seven"):
		return "7"
	elif(str(o) == "eight"):
		return "8"
	elif(str(o) == "nine"):
		return "9"
		
def tens1(t1):
	if(str(t1) == "one"):
		return "01"
	elif(str(t1) == "two"):
		return "02"
	elif(str(t1) == "three"):
		return "03"
	elif(str(t1) == "four"):
		return "04"
	elif(str(t1) == "five"):
		return "05"
	elif(str(t1) == "six"):
		return "06"
	elif(str(t1) == "seven"):
		return "07"
	elif(str(t1) == "eight"):
		return "08"
	elif(str(t1) == "nine"):
		return "09"
	elif(str(t1) == "ten"):
		return "10"
	elif(str(t1) == "eleven"):
		return "11"
	elif(str(t1) == "twelve"):
		return "12"
	elif(str(t1) == "thirteen"):
		return "13"
	elif(str(t1) == "fourteen"):
		return "14"
	elif(str(t1) == "fifteen"):
		return "15"
	elif(str(t1) == "sixteen"):
		return "16"
	elif(str(t1) == "seventeen"):
		return "17"
	elif(str(t1) == "eighteen"):
		return "18"
	elif(str(t1) == "nineteen"):
		return "19"
	elif(str(t1) == "twenty"):
		return "20"
	elif(str(t1) == "thirty"):
		return "30"
	elif(str(t1) == "forty"):
		return "40"
	elif(str(t1) == "fifty"):
		return "50"
	elif(str(t1) == "sixty"):
		return "60"
	elif(str(t1) == "seventy"):
		return "70"
	elif(str(t1) == "eighty"):
		return "80"
	elif(str(t1) == "ninety"):
		return "90"

def tens2(t2):
	if(str(t2) == "twenty"):
		return "2" 
	elif(str(t2) == "thirty"):
		return "3" 
	elif(str(t2) == "forty"):
		return "4" 
	elif(str(t2) == "fifty"):
		return "5" 
	elif(str(t2) == "sixty"):
		return "6" 
	elif(str(t2) == "seventy"):
		return "7" 
	elif(str(t2) == "eighty"):
		return "8" 
	elif(str(t2) == "ninety"):
		return "9" 
	
#wordsToNum
def wordsToNum1(w):
	#w = raw_input(" Enter a number: ")
	w = w.lower()
	toNum = " "
	
	while(str(w) != ""): #million
		if(w.find("million") != -1):
			ind = w.find("million")
			mi = w[0:ind+7] #include "million"
			ml = w[0:ind-1] #i-coconvert
			nextWord = w[len(mi)+1:] #tirang word #while()
			
			if(str(nextWord) == ""):
				toNum = str(toNum) + str(ones(ml)) + "000000"
			else:
				toNum = str(toNum) + str(ones(ml)) #num form
		elif(w.find("thousand") != -1):
			ind = w.find("thousand")
			th = w[0:ind+8] #include "million"
			tho = w[0:ind-1] #i-coconvert
			nextWord = w[len(th)+1:] #tirang word #while()
			
			if(tho.find("hundred") != -1):
				hunIn = tho.find("hundred")
				h1 = tho[0: hunIn+7]
				hun = tho[0: hunIn-1]
				hunNext = tho[len(h1)+1:]
				toNum = str(toNum) + str(ones(hun))              #print/include in toNum yung hundred thousandth digit
				
				if(str(hunNext) == ""):                          #wala nang kasunod yung hundred thousandth
					toNum = str(toNum) + "00000"
				else:      								 #may kasunod yung hundred thousandth     
					toNum = str(toNum) + str(tens1(hunNext))
			else:
				toNum = str(toNum) + "0" +str(tens1(tho))  
		elif(w.find("hundred") != -1):      
			hunIn = w.find("hundred")
			h1 = w[0: hunIn+7]
			hun = w[0: hunIn-1]
			nextWord = w[len(h1)+1:]
			toNum = str(toNum) + str(ones(hun))              #print/include in toNum yung hundred thousandth digit
				
			if(str(nextWord) == ""):                          #wala nang kasunod yung hundred thousandth
				toNum = str(toNum) + "00"
			else:      								 #may kasunod yung hundred thousandth     
				toNum = str(toNum) + str(tens1(nextWord))      
		w = nextWord
	##print toNum
	return toNum
	
def wordsToNum(a):
	print "Words to Number"
	print str(wordsToNum1(a))
	


def wordsToCurrency(word,cur):
	print "Words to Currency"
	if(cur == "USD" or cur == "JPY" or cur == "PHP"):
		print " " + str(cur) + str(wordsToNum1(word))
	else:
		print " Invalid currency"
		
def numberDelimited(number, dl, jmp):
	print "Number delimited"
	num1 = len(str(number))
	num2 = int(jmp)-2
	#num3 = int(num2) - 1
	word = str(number) + " "
	num4 = len(str(word))
	l = 0
	
	while(l <= jmp):
		word[l] = word[int(num1)-int(jmp)]
	if(jmp <= num1):
		word = str(dl) + str(word[num2:])
		print word
	else:
		print "Error"
	

#sample run
#numToWords()
wordsToNum(a = "one million twenty thousand one hundred")	
wordsToCurrency("one million twenty thousand one hundred", "USD")
numberDelimited(number = 1234,dl = ",", jmp = 2)
	




