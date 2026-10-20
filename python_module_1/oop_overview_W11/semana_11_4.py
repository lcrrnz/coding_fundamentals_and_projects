#Cree las siguientes clases: Head, Torso, Arm, Hand, Leg, Feet.
#Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

class Human:
    def __init__(self, torso):
        self.torso = torso
        print("You have assambled the forbibben one")


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg =right_leg
        self.left_leg = left_leg


class Head:
    def __init__(self):
        pass


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Hand:
    def __init__(self):
        pass


class Leg:
    def __init__(self, foot):
        self.foot = foot


class Foot:
    def __init__(self):
        pass


head = Head()
r_hand = Hand()
r_arm = Arm(r_hand)
l_hand = Hand()
l_arm = Arm(l_hand)
r_foot = Foot()
r_leg = Leg(r_foot)
l_foot = Foot()
l_leg = Leg(l_foot)
torso = Torso(head, r_arm, l_arm,r_leg, l_leg )
me = Human(torso)

