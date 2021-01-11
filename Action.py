import tello
import Perimeter_Sweep

class Action():
  def connectToDrone(self):
    print('Initilize connection to tello drone')
    self.drone = tello.Tello()
    print('Success connect to tello drone')
    return self.drone

  def getCurrentBattery(self):
    print('Obtain Current Battery Percentage')
    return self.drone.send("battery?", 3)

  # PrePlan Route
  def startPrePlanRoute(self):
    print('Start Pre Plan Route')
    Perimeter_Sweep.PrePlanRoute(self.drone).start()
    print('End Pre Plan Route')

  # Manual Control
  def takeOff(self):
    self.drone.send("takeoff", 7)
    print('Drone took off')

  def landing(self):
    self.drone.send("land", 7)
    print('Drone landed')

  # Direction=[up,down,left,right,forward,back]
  def move(self, direction, distance=50):
    moveCommand = direction + " " + str(distance)
    print('Drone moving {} cm'.format(moveCommand))
    self.drone.send(moveCommand, 5)

  # Direction=[cw(clockwise),ccw(counter clockwise)]
  def rotate(self, direction, angle=90):
    rotateCommand = direction + " " + str(angle)
    print('Drone rotate {}  degrees'.format(rotateCommand))
    self.drone.send(rotateCommand, 5)
