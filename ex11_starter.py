#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

#Make a line of hyphens the same length as the Belgium string
StringLength = len(Belgium)
print(str('-') * int(StringLength))

#Print the string with the comma separators replaced by colons
print(Belgium.replace(',', ':'))

#Print the population of Belgium (field 2) plus the population of the capital city (field 4)
BelgiumList = Belgium.split(',')
print(int(BelgiumList[1])+int(BelgiumList[3]))

