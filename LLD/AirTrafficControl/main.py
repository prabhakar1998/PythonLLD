from air_traffic_control import AirTrafficControl
from runway import Runway
from airplane import Airplane


# if __name__ == "__main__":
atc = AirTrafficControl("ATC1")
runway1 = Runway("Runway1", atc)
atc.add_runway(runway1)
runway2 = Runway("Runway2", atc)
atc.add_runway(runway2)

airplane1 = Airplane("Airplane1", atc)
airplane2 = Airplane("Airplane2", atc)
airplane3 = Airplane("Airplane3", atc)

airplane1.take_off_request()
airplane2.take_off_request()
airplane3.take_off_request()