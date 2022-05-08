# bit-by-bit-capstone
Team "Bit by Bit"'s Capstone Project. Our project is to help students learn the Java Cryptographic Library by means of providing a forum-like environment for them to ask questions. We also utilize NiCad to test similarity of code submittted. Our end goals include having admin accounts for professors and TA's to monitor the forum as well as improvements on the code differential UI. 


# Release Notes
Feb 28 2022 - M1 submission. Includes implementation of UI for question submission and browsing. Basic Django backend setup and full wireframe implementation. NiCad works in dev environment, although not on the webpage yet.  

Mar 23 2022 - M2 submission. Includes submittable forms as well as NiCad integration. Work was done in the front and back end to facilitate further improvement and functionality. 

Apr 6 2022 - M3 submission. Various work on inputting forms to database, imported sample data from client, question submission working, models finished, code submission to diff viewer working. NiCad XML integration with UI.

Apr 20 2022 - M4 Submission. Added questions viewed from database, testing for front and back end, documentation, reformatting code/database for given data


# Installation
Installation is simple using Docker.

Requirements:
 - A Ubuntu or Debian based system with Docker pre-installed. If you do not have Docker installed, follow the instructions here: https://docs.docker.com/engine/install/

Building and running the container:
1. Clone this repository onto your local system. 
2. ``docker build -t cryptotutor:v1 .``
3. ``docker run -d -p 8081:80 cryptotutor:v1``


# License
CryptoTutor - A question and answer forum with code comparison capabilities.
Copyright (C) 2022 Zoe Larson, Maya Lentsch, Tyler Bauer, Daniel Brinkman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.