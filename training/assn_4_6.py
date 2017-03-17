def computepay(h, r) :
    #print "In computepay h=", h, "r=", r
    if h <= 40 :
        p = r * h
    else :
        p = r * 40 + ( r * 1.5 *( h - 40) )
    #print 'Finished with compupay', p
    return p

try:
    inp = raw_input("Enter Hours: ")
    h = float(inp)
    inp = raw_input("Enter Rate: ")
    r = float(inp)
except:
    print "Error, please enter numeric input"
    quit()

#print "In the main code"
p = computepay(h, r)
print "Pay= ", p


