#CW 1
#Weston Smith

KNUTS_TO_SICKLES = 29
SICKLES_TO_GALLEONS = 17

inputKnuts = int(input("Enter the currency in knuts\n").strip())
totKnuts = inputKnuts

totSickles = totKnuts // KNUTS_TO_SICKLES
totKnuts = totKnuts % KNUTS_TO_SICKLES

totGalleons = totSickles // SICKLES_TO_GALLEONS
totSickles = totSickles % SICKLES_TO_GALLEONS

print(inputKnuts, "knuts =",totGalleons,"galleons", totSickles, "sickles", totKnuts, "knuts")