from pydantic import BaseModel

from floor import Floor


class SmartHouse (BaseModel):

    name: str
    floors: list[Floor]

    def read_floor(self, fid: int):

        for floor in self.floors:
            if floor.fid == fid:
                return floor

        return None

    def read_rooms(self, fid: int):

        floor = self.read_floor(fid)

        if floor:
            return floor.rooms

        return None

    def read_room(self, fid: int, rid: int):

        rooms = self.read_rooms(fid)

        if rooms:

            for room in rooms:
                if room.rid == rid:
                    return room

        return None

    def read_devices(self):

        floors = self.floors
        devices = list()

        for floor in floors:

            rooms = floor.rooms

            for room in rooms:

                devices.extend(room.devices)

        return devices

    def read_device(self, did):

        devices = self.read_devices()

        for device in devices:

            if device.did == did:
                return device

        return None
