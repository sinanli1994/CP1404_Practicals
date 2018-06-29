from taxi import Taxi
from taxi import UnreliableCar
from taxi import SilverServiceTaxi

# taxi1 = Taxi("Prius_1", 100)
# taxi1.drive(40)
# print(taxi1)
# taxi1.start_fare()
# taxi1.drive(100)
# print(taxi1)
#
# car1 = UnreliableCar(100, "car", 50)
# car1.drive(25)

silvertaxt = SilverServiceTaxi("silvertaxt", 100, 2)
silvertaxt.drive(10)
print(silvertaxt.get_fare())

