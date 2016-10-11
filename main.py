#
#
#
#

import csv
from random import randint
#with open('hotels.csv', 'wb') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ',
    #                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
name_praefix = [['Zum '],['Zur '],['Hotel ', 'Gasthaus ']]
name_middle  = [['','goldenen ', 'flotten ','durstigen ','pinken '],]
name_end     = [['Eber','Stier','Adler'],['Gans','Blume']]

print 'Start'

for name in range(0,20):
    rnd = randint(0,1)
    if(rnd == 0):
        rnd_1 = randint(0, 4)
        rnd_2 = randint(0, 2)
        print name_praefix[0][0] +name_middle[0][rnd_1] +name_end[0][rnd_2]
    if(rnd == 1):
        rnd_1 = randint(0, 4)
        rnd_2 = randint(0, 1)
        print name_praefix[1][0] +name_middle[0][rnd_1] +name_end[0][rnd_2]

