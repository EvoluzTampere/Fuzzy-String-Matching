text="Tampere on Suomen kaupunki ja Pirkanmaan maakuntakeskus rakas, joka sijaitsee Näsijärven ja Pyhäjärven rannoilla. Tampere on väkiluvultaan Suomen kolmanneksi suurin kunta ja lähikuntineen Suomen toiseksi suurin kaupunkialue. Tampere on myös asukasmäärältään Pohjoismaiden suurin sisämaakaupunki"
[ t for t in text.split('. ') if 'rakas' in t] #select the setence with word 'rakas'
text[0:100] #select the first 100 char.
