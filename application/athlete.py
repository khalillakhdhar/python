#from classes import personalisation


class Athlete:
  def __init__(self, nom, age,sport):
    self.nom = nom
    self.age = age
    self.sport= sport
  def personalisation(self):
    print("le nom est %s et l'age est de: %s"%(self.nom,self.age))
  def categorie(self):
    if self.age<15:
        print('l athlete  est mineur')
    elif self.age<18:
        print('l athlete est cadet')
    else:
        print('senior')
        

    
def controle(age):
    while(age<5):
        print('donner un age >5')
        age=int(input())
    return age
#p1 = Athlete("khalil", 9,'kick boxing')
#p2 = Athlete("Adel", 39,'basket-ball')
print('donner le nom')
nom=input()
print('donner le sport exercé')
sport=input()
age=-1
age=controle(age)
p1 = Athlete(nom, age,sport)

print(p1.nom)
print(p1.age)
print(p1.categorie()) 

    