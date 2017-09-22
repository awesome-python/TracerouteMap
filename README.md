# TracerouteMap
A simple Python script that shows a visual traceroute using Google Earth.

### Requirements
- Python 3.6
- Python Pip
- 32- or 64-bit Windows (currently NOT supporting Mac OS X or Linux)


### Installation
1. Clone (or download the ZIP) to your computer.
2. Run `install.py` to run the installation. This installs the latest Google Earth and simpleKML.
3. If installation went OK, you're good to go.


### How To Use
1. Using the command line (or a batch script), run:
    `python run.py <ip-address>`
2. Wait for the program to finish to traceroute.
3. It will open Google Earth when it is completed.


### FAQ
**Q:** What if I already have Google Earth installed?
**A:** Remove `os.system("GoogleEarthProSetup.exe")` from `install.py`.

**Q:** Why do I need Google Earth installed? Can't I just upload it to the web version?
**A:** You don't *need* it installed, it just streamlines the process for you. Just install simpleKML using `pip install` and execute `run.py`, ignoring the errors at the end (they mean they can't find Google Earth which makes sense), and upload the .kml file found in the program folder.

**Q:** Will Linux and Mac be supported in the future?
**A:** Yes. My reasoning is that Unix (Linux and Mac) have a different `traceroute` layout than Windows, and currently the Windows layout is easier to implement.