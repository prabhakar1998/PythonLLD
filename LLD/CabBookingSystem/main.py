import time
from CabBookingSystem.cab_booking_system import CabBookingSytem
from .consts import CabStatus, TripStatus
from CabBookingSystem.models.cab import CabEconomy
from CabBookingSystem.models.location import TwoDimentionalLocation
from CabBookingSystem.models.rider import Rider
from CabBookingSystem.strategies.booking_strategy import MaxDistanceBookingStrategy









if __name__ == "__main__":

    booking_strategy = MaxDistanceBookingStrategy(10)

    cbs = CabBookingSytem("Uber")

    rider1_location = TwoDimentionalLocation(0,0)
    rider1 = Rider("u1", "User1", rider1_location, cbs)
    cbs.register_rider(rider1)
    destination1 = TwoDimentionalLocation(3,22)


    cab1_location = TwoDimentionalLocation(1,1)
    cab1 = CabEconomy("Uber Rider1", "HR-01-0102", cab1_location, booking_strategy, CabStatus.StatusIdle)
    cbs.register_cab(cab1)
    trip1 = rider1.create_trip(destination1)

    if trip1 is not None:
        print("Cab is travelling towards the Rider")
        time.sleep(1)
        cab1.update_location(rider1_location)
        rider1.start_ride("1234")
        time.sleep(1)
        cab1.update_location(destination1)
        cab1.complete_trip()

    trips = rider1.get_trips()
    for trip in trips:
        if trip.status == TripStatus.Completed:
            trip.print()

    # driver is stopping the service
    cab1.status_off()
    rider2_location = TwoDimentionalLocation(3.5,23)
    rider2 = Rider("U2", "User2", rider1_location, cbs)
    cbs.register_rider(rider2)
    destination2 = TwoDimentionalLocation(3,22)
    trip2 = rider2.create_trip(destination1)