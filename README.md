# SchoolRouteFinder
 Simplifying school navigation with smart routes.

## Description
Ernest Bevin Route Finder is a project aimed at simplifying navigation within Ernest Bevin College using advanced routing algorithms and real-time data analysis. Say goodbye to crowded corridors and hello to efficient routes!

## Features
- Utilizes Dijkstra's algorithm for optimal pathfinding.
- Considers school schedules to provide timely routes between classes.
- Incorporates laser measurements for accurate mapping.

## Technologies Used
- Python
- PyQt5
- Dijkstra's algorithm
- Laser measurement tools
- CSV file handling

## Data Requirements
To run the Ernest Bevin Route Finder, you'll need:
- School layout maps
- Classroom locations
- Student schedules

## Project Setup and Usage
To set up the project, follow these steps:
1. Make sure you have Python installed on your system.
2. Install PyQt5 using `pip install PyQt5`.
3. Run the `main.py` file to launch the application.

**Usage Instructions:**
- Depending on the feature you'd like to utilize, you will need to create either a text file or an Excel file in the same format as the ones provided in this repository.
- For optimal results, ensure that the data in your files matches the expected format.

-For text file format which shows the fastest route between two points of the school map:
	![Alt text](/understandingtextfile.png?raw=true)

-For excel file format which shows the entire route based on the students classes for the day:
	![Alt text](/understandingexcelfile.png?raw=true)
