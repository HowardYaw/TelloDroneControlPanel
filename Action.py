import tello
import Perimeter_Sweep

class Action:  

  def connectToDrone(self):
    print('Initilize connection to tello drone')
    self.drone = tello.Tello()
    print('Success connect to tello drone')

  def startPerPlanRoute(self):
    print('Start Pre Plan Route')
    Perimeter_Sweep.PrePlanRoute(self.drone).start()
    print('End Pre Plan Route')


