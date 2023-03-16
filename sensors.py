import abc
from typing import Optional

from device import Device


class Sensor(Device):

    def is_sensor(self):
        return True

    def is_actuator(self):
        return False

    @abc.abstractmethod
    def get_current_value(self):
        pass

    @abc.abstractmethod
    def set_current_value(self, value: float):
        pass


class TemperatureSensor(Sensor):

    temperature: float | None = None
    unit: str | None = "°C"

    def get_current_value(self) -> Optional[float]:
        return self.temperature

    def set_current_value(self, temperature: float):
        self.temperature = temperature


class HumiditySensor(Sensor):

    humidity: float | None = None
    unit: str | None = "%"

    def get_current_value(self) -> Optional[float]:
        return self.humidity

    def set_current_value(self, humidity: float):
        self.humidity = humidity


class SmartMeter(Sensor):

    energy_consumption: float | None = None
    unit: str | None = "kWh"

    def get_current_value(self) -> Optional[float]:
        return self.energy_consumption

    def set_current_value(self, energy_consumption: float):
        self.energy_consumption = energy_consumption


class AirQualitySensor(Sensor):

    air_quality: float | None = None
    unit: str | None = "g/m^2"

    def get_current_value(self) -> Optional[float]:
        return self.air_quality

    def set_current_value(self, air_quality: float):
        self.air_quality = air_quality

