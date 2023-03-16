from typing import Optional
import abc

from device import Device


class Actuator(Device):

    def is_actuator(self):
        return True

    def is_sensor(self):
        return False

    @abc.abstractmethod
    def get_current_state(self):
        pass

    @abc.abstractmethod
    def set_current_state(self, value):
        pass


class SimpleOnOffActuator(Actuator):

    is_active: bool | None = False

    def get_current_state(self):
        return self.is_active

    def set_current_state(self, is_active):
        self.is_active = is_active


class HeatControlActuator(Actuator):

    temperature: float | None = 18.5

    def get_current_state(self):
        return self.temperature

    def set_current_state(self, temperature):
        self.temperature = temperature


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

