from pricing_stratergy import PricingStratergy
from vehicle import Vehicle
from helpers import ms_to_hr
import math

class TimeRangePricingStratergy(PricingStratergy):

    def get_price(self, vehicle: Vehicle, entry_time: float, exit_time: float) -> float:
        price = 5 # default min price

        hourly_price = vehicle.get_hourly_price()
        duration_ms = exit_time - entry_time
        parked_hours = ms_to_hr(duration_ms)
        if parked_hours < 1:
            price = hourly_price
        elif 1 <= parked_hours >= 12:
            # half day pricing
            price = hourly_price * 4
        elif 12 <= parked_hours >= 24:
            # full day pricing            
            price = hourly_price * 6
        elif parked_hours > 24:
            # long days pricing
            days = math.ceil(parked_hours / 24)
            price = hourly_price * 5 * days
        return price
