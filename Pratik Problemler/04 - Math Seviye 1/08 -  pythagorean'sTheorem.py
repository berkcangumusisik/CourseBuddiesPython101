""" Pisagor Teoremi
2 bacak uzunluğu verilen bir üçgenin hipotenüsünü bulmak için Pisagor 
Teoremini kullanacak bir fonksiyon yazın.

Unutma, Pisagor Teoremi: hyp^2 = bacak^2 + bacak^2
"""

from math import *
def pythag_theorem(leg1, leg2):
    hyp = sqrt(leg2*leg2 + leg1 * leg1)
    return hyp

print(pythag_theorem(3,4))
