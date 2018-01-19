import md5
import random

sentence = "The quick brown fox jumps over the internetz"

print "start"
def hashMe(plainText):
    m = md5.md5()
    m.update(plainText)
    return m.hexdigest()

def encrypt(plainText):
    derp = "::"
    for i in plainText:
        derp += hashMe(hashMe(str(random.randint(1, 100))+i))
        derp += "::"
    return derp

def decrypt(chiper):
    plain = ""
    print "Checkpoint"
    for imp in chiper:
        print imp
        try:
            for b in range(1, 100):
                print "Checking", b
                for a in range(1, 200):
                    #print "compare", hashMe(hashMe(str(b)+chr(a))), "With", i
                    if hashMe(hashMe(str(b)+chr(a))) == imp:
                        print "Debug hash check returned true:", chr(a)
                        plain += chr(a)
        except e:
            print e
        return plain

        

a = encrypt(sentence)
print a
print "End"

