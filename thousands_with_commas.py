
def thousands_with_commas(i):
    i = unicode(str(i), 'utf-8')
    if i.isnumeric() is True:

        j  = i[::-1]
        j = [char for char in j]
        k = []
        for index, char in enumerate(j):
            k.append(char)
            if (index+1)%3 == 0 and index < (len(i)-1):
                k.append(',')
        k = ''.join(k)
        k = k[::-1] 
                   
        print k
        return str(k)
    else:
        print 'string isnt numeric'

if __name__ == '__main__':

    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
