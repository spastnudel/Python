text = "X-DSPAM-Confidence:    0.8475";
first_num = text.find ('0')
last_num = text.find ('5')
number = text[first_num -1 : last_num + 1]
number = float(number)
print number