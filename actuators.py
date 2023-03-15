from typing import Optional

from device import Device


class Actuator(Device):

    def is_actuator(self):
        return True

    def is_sensor(self):
        return False


class SimpleOnOffActuator(Actuator):

    is_active: bool | None = False


class HeatControlActuator(Actuator):

    temperature: float | None = 18.5


class HeatOven(HeatControlActuator):
    pass


class LightBulb(SimpleOnOffActuator):
 
    pass


class SmartOutlet(SimpleOnOffActuator):

    pass


class SmartCharger(SimpleOnOffActuator):

    pass


class Dehumidifier(SimpleOnOffActuator):

    pass


class HeatPump(HeatControlActuator):

    pass


class FloorHeatingPanel(HeatControlActuator):

    pass

