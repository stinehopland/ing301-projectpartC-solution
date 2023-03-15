from typing import Optional

from device import Device


class Sensor(Device):

    def is_sensor(self):
        return True

    def is_actuator(self):
        return False


class TemperatureSensor(Sensor):

    temperature: float | None = None
    unit: str | None = "°C"

    def get_current_value(self) -> Optional[float]:
        return self.temperature


class HumiditySensor(Sensor):

    humidity: float | None = None
    unit: str | None = "%"

    def get_current_value(self) -> Optional[float]:
        return self.humidity


class SmartMeter(Sensor):

    energy_consumption: float | None = None
    unit: str | None = "kWh"

    def get_current_value(self) -> Optional[float]:
        return self.energy_consumption


class AirQualitySensor(Sensor):
    air_quality: float | None = None
    unit: str | None = "g/m^2"
