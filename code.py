class Car(object):
    def __init__(self,model,color,company,speed_limit) :
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.model=model

    def start(self):
        print("started")

    def stop(self):
        print("stoped")

    def accelarate(self):
        print("accelarating")


audi = Car("2020","red","honda","180")
print(audi.color)
print(audi.model)
audi.stop()

duster = Car("1999","black","Honda","500")
print(duster.company)
duster.accelarate()

