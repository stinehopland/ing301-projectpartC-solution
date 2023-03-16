# Install FastAPI framework
# pip3 install "fastapi[all]"
# https://fastapi.tiangolo.com/tutorial/

# uvicorn main:app --reload

from fastapi import FastAPI, Response, status
from fastapi.staticfiles import StaticFiles

from demohouse import build_demo_house
from device import Device
from sensors import *
from actuators import *


app = FastAPI()

# http://localhost:8000/welcome/index.html
app.mount("/welcome", StaticFiles(directory="static"), name="static")


smart_house = build_demo_house()


def create_response(body, response: Response, status_code):

    if body:
        return body

    response.status_code = status_code

    return None


# http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Welcome to SmartHouse Cloud REST API - Powered by FastAPI"}


@app.get("/smarthouse")
async def read_smart_house(response: Response):
    return create_response(smart_house, response, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/floor/")
async def read_smart_house(response: Response):
    return create_response(smart_house.floors, response, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/floor/{fid}")
async def read_floor(fid: int, response: Response):

    floor = smart_house.read_floor(fid)

    return create_response(floor, response, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/floor/{fid}/room/")
async def read_rooms(fid: int, response: Response):

    rooms = smart_house.read_rooms(fid)

    return create_response(rooms, response, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/floor/{fid}/room/{rid}")
async def read_room(fid: int, rid: int, response: Response):

    room = smart_house.read_room(fid, rid)

    return create_response(room, response, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/device")
async def read_devices(response: Response):

    devices = smart_house.read_devices()

    return create_response(devices, response, status.HTTP_404_NOT_FOUND)


@app.get("/smarthouse/device/{did}")
async def read_device(did: int, response: Response):

    device = smart_house.read_device(did)

    return create_response(device, response, status.HTTP_404_NOT_FOUND)


@app.post("/smarthouse/room/{rid}/device/")
async def create_device(rid: int, device: TemperatureSensor):

    room = smart_house.find_room(rid)

    if room:
        room.devices.append(device)

        return room

    return None


@app.get("/smarthouse/sensor/{did}/current")
async def read_current_value(did: int):

    device = smart_house.read_device(did)

    if device and device.is_sensor():
        return SensorMeasurement(value=str(device.get_current_value()))

    return None


@app.post("/smarthouse/sensor/{did}/current")
async def update_current_value(did: int, measurement: SensorMeasurement):

    device = smart_house.read_device(did)

    if device and device.is_sensor():
        device.set_current_value(float(measurement.value))

    return device


@app.delete("/smarthouse/sensor/{did}/oldest")
async def delete_device(did: int, response: Response):

    device = smart_house.read_device(did)

    if device and device.is_sensor():
        device.delete_oldest_value()

    return device


@app.get("/smarthouse/actuator/{did}/current")
async def read_current_state(did: int):

    device = smart_house.read_device(did)

    if device and device.is_actuator():
        return ActuatorState(state=device.get_current_state())

    return None

@app.put("/smarthouse/actuator/{did}/current")
async def update_current_state(did: int, state: ActuatorState, response: Response):

    device = smart_house.read_device(did)

    if device and device.is_actuator():
        device.set_current_state(state.state)

    return device
