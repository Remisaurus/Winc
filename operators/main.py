# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line


#sp for spain , sw for switserland
languagesp='Spanish'
languagesw='German'+'French'
prevailingreligionsp='Roman Catholic'
prevailingreligionsw='Roman Catholic'
capitalsp='Madrid'
capitalsw='Bern'
GDPsp=1714860000000
GDPsw=590710000000
popgrowsp=0.13
popgrowsw=0.65
popsp=47163418
popsw=8508698

print(languagesp==languagesw)
print(prevailingreligionsp==prevailingreligionsw)
print(len(capitalsp)!=len(capitalsw))
print(GDPsw>GDPsp)
print (popgrowsp<1 and popgrowsw<1)
print(popsp>10000000 or popsw>10000000)
print((popsp>10000000 and popsw<10000000) or (popsp<10000000 and popsw>10000000))