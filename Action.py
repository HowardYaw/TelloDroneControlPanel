import tello
import Perimeter_Sweep


def connectToDrone():
  print('Initilize connection to tello drone')
  self.drone = tello.Tello()
  print('Success connect to tello drone')

def startPerPlanRoute():
  print('Start Pre Plan Route')
  Perimeter_Sweep.PrePlanRoute(self.drone).start()
  print('End Pre Plan Route')


