# bit-by-bit-capstone
Team "Bit by Bit"'s Capstone Project. Our project is to help students learn the Java Cryptographic Library by means of providing a forum-like environment for them to ask questions. We also utilize NiCad to test similarity of code submittted. Our end goals include having admin accounts for professors and TA's to monitor the forum as well as improvements on the code differential UI. 


# Release Notes
Feb 28 2022 - M1 submission. Includes implementation of UI for question submission and browsing. Basic Django backend setup and full wireframe implementation. NiCad works in dev environment, although not on the webpage yet.  

Mar 23 2022 - M2 submission. Includes submittable forms as well as NiCad integration. Work was done in the front and back end to facilitate further improvement and functionality. 

Apr 6 2022 - M3 submission. Various work on inputting forms to database, imported sample data from client, question submission working, models finished, code submission to diff viewer working. NiCad XML integration with UI.

Apr 20 2022 - M4 Submission. Added questions viewed from database, testing for front and back end, documentation, reformatting code/database for given data

May 11 2022 - M5 Final Submission - For this milestone, many small tasks were finished and polished, including code cleanup, bug squashing, testing, and various feature implementation such as question deletion and question sorting for the main page.  

# Installation
Installation is simple using Docker.

Requirements:
 - A Ubuntu or Debian based system with Docker pre-installed. If you do not have Docker installed, follow the instructions here: https://docs.docker.com/engine/install/
 - Python 3.9 is needed for this project.
 - Install needed packages: ```sudo apt install build-essential python3-pip python3-django python-is-python3 wget g++ git```
 - Build FreeTXL: ```sudo mkdir /tmp/freetxl-build/ && cd /tmp/freetxl-build && sudo wget http://www.txl.ca/download/29321-txl10.8a.linux64.tar.gz && sudo tar -xvf 29321-txl10.8a.linux64.tar.gz```
 - ```cd /tmp/freetxl-build/txl10.8a.linux64/ && sudo ./InstallTxl```
 - ```sudo rm -rf /tmp/freetxl-build```
 - Build NiCad: ```sudo mkdir /tmp/nicad-build/ && cd /tmp/nicad-build && sudo wget http://www.txl.ca/download/5659-NiCad-6.2.tar.gz && sudo tar -xvf 5659-NiCad-6.2.tar.gz```
 - ```cd /tmp/nicad-build/NiCad-6.2 && sudo make```
 - ```sudo mkdir /usr/local/lib/nicad6 && sudo cp -r /tmp/nicad-build/NiCad-6.2/* /usr/local/lib/nicad6```
 - ```sudo sed -i 's/LIB=./LIB=\/usr\/local\/lib\/nicad6/g' /tmp/nicad-build/NiCad-6.2/nicad6```
 - ```sudo sed -i 's/LIB=./LIB=\/usr\/local\/lib\/nicad6/g' /tmp/nicad-build/NiCad-6.2/nicad6cross```
 - ```sudo cp /tmp/nicad-build/NiCad-6.2/nicad6 /usr/local/bin/```
 - ```sudo cp /tmp/nicad-build/NiCad-6.2/nicad6cross /usr/local/bin```
 - ```sudo chmod +x /usr/local/bin/nicad6```
 - ```sudo chmod +x /usr/local/bin/nicad6cross```
 - ```sudo rm -rf /tmp/nicad-build```
 
Setting up the project:
1. Users must install the specified apps from the requirement-file by running ```pip install -r requirement_file.txt```
2. In order to run code comparisons using NiCad, please ensure that the config files under the "nicad_configs" folder are included in the config folder at the NiCad installation location (ie usr/local/lib/nicad6/config). These commands will copy the nicad_config folder into the nicad6 config folder, then move the config files out of the nicad_config folder and into the config folder, before removing the now-empty nicad_configs folder. This should be done with the following commands:
3. ```sudo cp -a /path/to/cryptotutor/nicad_configs /path/to/nicad6/config ```
4. ```cd nicad_configs```
5. ```sudo mv * ..```
6. ```cd ..```
7. ```sudo rm -rf nicad_configs```
8. In order to use Firefox for front end testing, the user must ensure that their geckodriver file is located in the /usr/local/bin/geckodriver file path, or they must change that line to match their geckodriver location. In order to run the test, the user must navigate into the cryptotutor file in the terminal before running the following commands: 
9. ```export PYTHONPATH=~/path/to/capstone```
10. ```export DJANGO_SETTINGS_MODULE=capstone.settings```
11. ```behave```
12. In order to run the project locally, run the command:
13. ```python3 manage.py runserver```
14. If there are multiple python versions. Otherwise, replace python3 with python. Alternatively, the user could run:
15. ```sudo apt install python-is-python3```
16. before running the run server command

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
