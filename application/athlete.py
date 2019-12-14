#from classes import personalisation


class Athlete:
  def __init__(self, nom, age,sport):
    self.nom = nom
    self.age = age
    self.sport= sport
  def personalisation(self):
    print("le nom est %s et l'age est de: %s"%(self.nom,self.age))
  def categorie(self,age):
    if age<15:
        print('l athlete  est mineur')
    elif age<18:
        print('l athlete est cadet')
    else:
        print('senior')
        

    

p1 = Athlete("khalil", 29,'kick boxing')
p2 = Athlete("Adel", 39,'basket-ball')

print(p1.nom)
print(p1.age)
print(p2.categorie(p2.age)) 