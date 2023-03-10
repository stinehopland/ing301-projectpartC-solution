# ING301 prosjekt - Del C

I del C av prosjektet skal dere implementere en REST API for en SmartHus sky-tjeneste ved bruk av rammeverket [FastAPI](https://fastapi.tiangolo.com)

## Setup og startkode

Startkoden for prosjektet finnes i dette github repository 

TODO LENKE

some dere kan bruke som mal (Use as Template) tilsvarende tidligere startkode for prosjektene. Startkoden inneholder klasser for devices og sensors samt konstruksjon av smarthus demo eksemplet. Om dere vil kan dere utskifte klassene med de klassene som dere selv har utvikler i prosjekt A og prosjekt B. 

I prosjekt C skal vi ikke integrere data-basen delen. Det er planen at dette skal gjøres i Del D sammen med implementasjon av klient-applikasjoner som bruker REST API'et utviklet i denne del av prosjektet.

For å kunne bruke FastAPI rammeverket skal dette først installeres. Dette kan gjøres med:

```
pip3 install "fastapi[all]"
```

For å gjøre tjenesten som utvikles og for å laste den på nytt når der gjøre endringer i koden kan følgende brukes:

```
uvicorn main:app --reload
```

som gjør at tjenesten settes i drift ved å bruke `uvicorn` web-tjeneren. 

For løsning av oppgaven kan det være en god ide å søke inspiration i eksemplet fra forelesningen i uke 12 der FastAPI ble brukt til å utvikle en REST API for sykkelcomputer eksemplet:

Koden finnes her:

TODO LENKE

Der er også hjelp å hente i dokumentasjonen for FastAPI som finnes via:

https://fastapi.tiangolo.com

REST API'et skal dere teste ved å skrive noen test i [Postman](https://www.postman.com) verktøyet som også blev demonstrert på forelesningen i uke 11. 

TODO: lenke til video

## REST API endepunkter

REST API'et som skal utvikles skal gjøre det mulig å hente informasjon om oppbygging av smarthuset viat følgene API endepunkter som alle skal returnere et svar i JSON-format.


- `GET smarthouse/floor` - information on all floors

- `GET smarthouse/floor/{fid}` - information about a floor given by `fid` including rooms ids
 
- `GET smarthouse/floor/{fid}/room/` - information about all rooms on a given floor

- `GET smarthouse/floor/{fid}/room/{rid}`- information about a specific room on a given floor including device ids

Videre skal API'et ha følgende endepunkter for tilgang til devices (sensorer og aktuatorer)

- `GET smarthouse/device` - information on all devices

- `GET smarthouse/device/{did}` - get information for a given device - meta information + current state (actuator) + current measurement (sensor)

- `GET smarthouse/device/{did}/measurements?count=>n>` - get n latest measurements from a device SENSOR vs. ACTUATOR?

- `POST smarthouse/room/{rid}/device` - add new device in a room - will return representation including new id

- `PUT smarthouse/device/{id}` - update a device - should we handle control this way on a actuator?

- `DELETE smarthouse/device/{id}` - delete a device

## Levering av prosjekt

- Linke til github repo
- Linke til eksport json test fil fra Postman
- Kan postman tester kjøres som del av github actions? https://medium.com/@liams_o/postman-tests-in-github-actions-pipeline-cd0adadf3dd2