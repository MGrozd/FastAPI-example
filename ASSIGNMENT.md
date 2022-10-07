# nuvolar_works_assignment
## Novular assignment

**Specifications**

The customer needs a way to efficiently manage their aircraft fleet. You are a member of the backend team in charge of this project.

It has been agreed that the minimum viable product would provide a REST API to perform CRUD operations on the fleet.

**Requirements**

- Aircraft are represented by a unique serial number and a manufacturer (those two attributes can be represented as strings)

- An aircraft can be assigned to a flight. A flight is represented by:

  - A departure and an arrival airport (airports are represented using their ICAO codes - see here for more information: https://en.wikipedia.org/wiki/ICAO_airport_code)

  - Departure and arrival dates and times

  - An aircraft, that can be assigned to the flight at its creation or later

- A flight can only be created for a future departure

- Flights can be searched by departure and arrival airport, as well as a departure time range.

**Nice to have**

- For reporting purposes, it would be useful to have the ability to retrieve, for a given period of time (departure and arrival datetime interval, provided as request parameters), the list of the departure airports of all flights flying - partially or not - within this time range, and for each departure airport, the number of flights as well as the in-flight time for each aircraft. The in-flight time taken into account should be strictly within the time range, and the average time is expressed in minutes.

**Technical considerations**

- This backend has to be developed in Python (any version starting at 2.7 or newer is fine), The web framework you use is completely up to you

- There is no need for a UI, but make sure to document your API to ease QA work (a good README.md embedding the endpoints description is enough)

- Unit tests, code quality and compliance with standard conventions, and documentation will be considered.

- You can either push your solution to the repository of your choice or send it as a zip file. However, if you choose to provide a Git repository, please make sure you keep it private and provide access to the person in charge of your application.
