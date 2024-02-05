import sys, heapq, csv
#from docx import Document
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

class MainPage(QMainWindow):
    
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('MainMenu.ui', self)
        self.year7.clicked.connect(self.openYear7)
        self.oneRoute.clicked.connect(self.openRoute)

    def openYear7(self):
        loadUi('year7.ui', self)
        self.backButton.clicked.connect(self.back)
        self.tutorPickCombo.addItems(["ABA","YC","JRS","AN"
                                      ,"GS","GO","JLS"])
        self.dayBox.addItems(["Monday","Tuesday","Wednesday",
                              "Thursday","Friday"])
        self.selectButton.clicked.connect(self.buttonClicked)

    def openRoute(self):
        loadUi('route.ui', self)
        self.backButton.clicked.connect(self.back)
        self.FindButton.clicked.connect(self.retrieveText)

    def back(self):
        loadUi('MainMenu.ui', self)
        self.year7.clicked.connect(self.openYear7)
        self.oneRoute.clicked.connect(self.openRoute)

    def buttonClicked(self):
        
        self.TutorPicked = self.tutorPickCombo.currentText()
        self.DayPicked = self.dayBox.currentText()
        startVal, row = checkTutor(self.TutorPicked)
        listOfPeriods = ["From Tutor to Period 1",
                         "From Period 1 to Period 2",
                         "From Period 2 to Period 3",
                         "From Period 3 to Period 4",
                         "From Period 4 to Period 5",
                         "From Period 5 to Period 6"]
        self.Week = reader(row, startVal)
        Route = ""
        index = 0
        
        if self.DayPicked == "Monday":
            dayIndex = 0
        elif self.DayPicked == "Tuesday":
            dayIndex = 1
        elif self.DayPicked == "Wednesday":
            dayIndex = 2
        elif self.DayPicked == "Thursday":
            dayIndex = 3
        elif self.DayPicked == "Friday":
            dayIndex = 4
            
        for period in self.Week[dayIndex]:
            Route = Route + "\n" + listOfPeriods[index] + "\n"
            for route in period:
                Route = Route + route + "\n"
            index+=1
        self.RouteOutput.setText(Route)
        self.WordButton.clicked.connect(self.wordClicked)

    def wordClicked(self):
        writeToWord(self.Week, self.TutorPicked)
        

    def retrieveText(self):
        
        start = self.startInput.toPlainText()
        end = self.endInput.toPlainText()
        route = retrieveRoute(start, end)
        
        if route == "No value":
            self.outputResult.setText("That is not a valid option")
        else:
            Route = ""
            for i in route:
                Route = Route + i + "\n"
            Route = Route[:-1]
            self.outputResult.setText(Route)



class Edge():

    def __init__(self, distance, startVertex, endVertex):
        self.distance = distance
        self.startVertex = startVertex
        self.endVertex = endVertex


class Node():

    def __init__(self, room):
        self.room = room
        self.visited = False
        self.child = None
        self.allEdges = []
        self.minDistance = 1000000000

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority


class Dijkstras():
    
    def __init__(self):
        self.route = []
        
    def calcShortestRoute(self, graph, startVertex):
        queue = []
        startVertex.minDistance = 0
        heapq.heappush(queue, startVertex)
        
        while queue:
            actualVertex = heapq.heappop(queue)
            
            for edge in actualVertex.allEdges:
                initial = edge.startVertex
                final = edge.endVertex
                newDistance = initial.minDistance + edge.distance
                if newDistance < final.minDistance:
                    final.child = initial
                    final.minDistance = newDistance
                    heapq.heappush(queue,final)
                else:
                    pass

    def routeToEndVertex(self, endVertex):
        print("Shortest Path to room is:", endVertex.minDistance,"m")
        node = endVertex
        
        while node is not None:
            self.route.append(node.room)
            node = node.child
        self.route.reverse()
        return self.route



def nodefinder():
    global nodes
    nodes = []
    with open('Rooms.txt') as f:
        for i in f:
              nodes.append(i)
   

def createGraph():
    nodeId = 1
    edgeId = 1
    count = 0
    nodeVal = 0
    edgeVal = 0
    position = 0
    graph = []
    edgelist = []
    nodefinder()
    x = True
    while x == True:
        
        count = 0
        while position<len(nodes):
            
            count = 0
            tempnode = nodes[position]
            for i in tempnode:
                
                if i == "(":
                    man = 0
                    mainNode = tempnode[0:count]
                    true = True
                    if graph == []:
                        graph.append("Node"+str(nodeId))
                        graph[nodeVal] = Node(mainNode)
                        nodeId += 1
                        count += 1
                        c = count
                        nodeVal += 1
                    else:
                        for node in graph:
                            if mainNode == node.room:
                                true = False
                            else:
                                if true == True:
                                    man += 1
                                else:
                                    pass                                   
                        if true == True:
                            graph.append("Node" + str(nodeId))
                            mainNode = tempnode[0:count]
                            graph[nodeVal] = Node(mainNode)
                            nodeId += 1
                            count += 1
                            c = count
                            nodeVal += 1
                        else:
                            count+=1
                            c = count

                if i == ":":
                    true = True
                    chil = 0
                    child = tempnode[c:count-1]
                    for node in graph:
                        if child == node.room:
                            true = False
                        else:
                            if true == True:
                                chil+=1
                            else:
                                pass
                    if true == True:
                        graph.append("Node" + str(nodeId))
                        graph[nodeVal] = Node(child)
                        nodeId += 1
                        nodeVal += 1
                        c = count
                    else:
                        c = count
                        
                if i == ",":
                    distance = tempnode[c:count-1]
                    edgelist.append("Edge" + str(edgeId))
                    edgelist[edgeVal] = Edge(float(distance),graph[man],graph[chil])
                    graph[man].allEdges.append(edgelist[edgeVal])
                    edgeId+=1
                    edgeVal+=1
                    edgelist.append("Edge" + str(edgeId))
                    edgelist[edgeVal] = Edge(float(distance),graph[chil],graph[man])
                    graph[chil].allEdges.append(edgelist[edgeVal])
                    edgeVal+=1
                    edgeId+=1
                    c = count
                    
                if i == ")":
                    distance = tempnode[c:count-1]
                    edgelist.append("Edge" + str(edgeId))
                    edgelist[edgeVal] = Edge(float(distance),graph[man],graph[chil])
                    graph[man].allEdges.append(edgelist[edgeVal])
                    edgeId+=1
                    edgelist[edgeVal] = Edge(float(distance),graph[chil],graph[man])
                    graph[chil].allEdges.append(edgelist[edgeVal])
                    position+=1
                    edgeId+=1
                    edgeVal+=1
                else:
                    count+=1
                x = False
                
        return(graph)


def retrieveRoute(start, end):
    
    aRoute = Dijkstras()
    graph = createGraph()
    startVal = str(roomNum(start))
    endVal = str(roomNum(end))
    if (startVal == "inc"):
        return "No value"
    else:
        for node in graph:
            if startVal == node.room:
                aRoute.calcShortestRoute(graph,node)
            else:
                pass
            
        for node in graph:
            if endVal == node.room:
                route = aRoute.routeToEndVertex(node)
        return route



def checkTutor(tutee):
    
    start = ""
    x = False     
    if tutee == "ABA":
        start = "Rm 38-39"
        row = 12
    elif tutee == "YC":
        start = "Rm 36-37"
        row = 18
    elif tutee == "JRS":
        start = "Science Corridor 1"
        row = 6
    elif tutee == "AN":
        start = "Rm 301-305"
        row = 30
    elif tutee == "GS":
        start = "Rm 108-110"
        row = 21
    elif tutee == "GO":
        start = "Rm 117-122"
        row = 9
    elif tutee == "JLS":
        start = "Rm 108-110"
        row = 24
    else:
        pass
    return start, row
 

def roomNum(val):
    
    if val.isdigit() == True:
        val = int(val)
        if val in range(301, 306):
            val = "Rm 301-305"
        elif val in range(306, 312):
            val = "Rm 306-311"
        elif val in range(311, 316):
            val = "Rm 310-315"
        elif val in range(201,205):
            val = "Rm 201-204"
        elif val in range(205, 212):
            val = "Rm 205-211"
        elif val in range(212, 218):
            val = "Rm 212-217"
        elif val in range (101,105):
            val = "Rm 101-104"
        elif val in range(108, 111):
            val = "Rm 108-110"
        elif val == 116:
            val = "Rm 116"
        elif val in range(117, 123):
            val = "Rm 117-122"
        elif val == 9:
            val = "Rm 9"
        elif val == (10 or 11):
            val = "Rm 10-11"
        elif val in range(1, 4):
            val = "Rm 1-3"
        elif val in range(36,38):
            val = "Rm 36-37"
        elif val in range(38,40):
            val = "Rm 38-39"
        elif val == 44:
            val = "Referral"
        elif val in range(32, 36):
            val = "Science Corridor 1"
        elif val in range(28, 32):
            val = "Science Corridor 2"
        elif val in range(24, 28):
            val = "Science Corridor 3"
        elif val in range(17, 24):
            val = "Science/Art Corridor"
        elif val == 17:
            val = "Rm 17"
        elif val in range(40, 44):
            val = "Rm 40-43"
        elif val in range(13,15):
            val = "Rm 13-14"
        elif val == 12:
            val = "Rm 12"
        elif val == (106 or 107):
            val = "Ch 106-107"
        elif val in range (103,105):
            val = "Rm 103-104"
        else:
            val = "inc"
            
    elif val.isdigit() == False:
        val = str(val)
        if val == ("reception"):
            val = "Reception"
        elif ("staff" in val):
            val = "Staff"
        elif val == ("offices"):
            val = "Offices"
        elif val == ("canteen"):
            val = "Canteen"
        elif val == ("pupil" or "entrance" or "pupil entrance"):
            val = "Pupil"
        elif val == ("hall"):
            val = "Hall"
        elif val == ("referral"):
            val = "Referral"
        elif val == ("courtyard"):
            val = "CourtyardS"
        elif val == ("medical"):
            val = "Medical"
        elif val == ("sports" or "sports hall"):
            val = "Sports Hall"
        elif val == ("gym"):
            val = "Gym"
        elif val == ("dojo"):
            val = "Dojo"
        elif val == ("study"):
            val = "Study"
        elif (val == "SFC"):
            val = "SFC"
        elif val == "FLD1":
            val = "B"
        elif val == ("FLD2"):
            val = "B"
        elif val == "GYM1":
            val = "Gym"
        elif val == "GYM2":
            val = "Gym"
        elif val == "Library":
            val = "Library"
        elif val == "SPH1":
            val = "Sports Hall"
        else:
            val = "inc"
    return val
     

def reader(row, start):
    
    graph = createGraph()
    index = 0
    listOfRooms = []
    route = ["MONP1","MONP2","MONP3","MONP4","MONP5","MONP6",
             "TUEP1","TUEP2","TUEP3","TUEP4","TUEP5","TUEP6",
             "WEDP1","WEDP2","WEDP3","WEDP4","WEDP5","WEDP6",
             "THUP1","THUP2","THUP3","THUP4","THUP5","THUP6",
             "FRIP1","FRIP2","FRIP3","FRIP4","FRIP5","FRIP6"]
    
    with open('Whole.csv','r') as f:
        
        file = csv.reader(f)
        rows = [r for r in file]

    for i in range(32):
        rows[i] = ([s.strip('\xa0') for s in rows[i]])
    
    for i in range(1,35):
        if rows[4][i] == "":
            listOfRooms.append(start)
        else:
            listOfRooms.append(roomNum(rows[row][i]))


    listOfRooms = [start] + listOfRooms
    
    while len(listOfRooms) != 1:
        route[index] = Dijkstras()
        
        for node in graph:
            if listOfRooms[0] == node.room:
                route[index].calcShortestRoute(graph,node)
            else:
                pass
            
        for node in graph:
            if listOfRooms[1] == node.room:
                Route = route[index].routeToEndVertex(node)
                route[index] = Route
            else:
                pass
        graph = createGraph()
        index +=1
        listOfRooms.pop(0)
        if len(listOfRooms) == 1:
            break
        else:
            if listOfRooms[1] == start:
                listOfRooms.pop(0)
    
    Mon = route[:6]
    Tue = route[6:12]
    Wed = route[12:18]
    Thu = route[18:24]
    Fri = route[24:30]
    
    Week = [Mon,Tue,Wed,Thu,Fri]
    return Week

def writeToWord(week,tutorGroup):

    document = Document()
    document.add_heading('\t\t\t\t\tTime table for ' + tutorGroup)
    document.add_paragraph('\t\t  Mon\t\t  Tue\t\t  Wed\t\t  Thu\t\t  Fri')
    table = document.add_table(rows=6, cols=6, style='Table Grid')
    
    row = table.rows[0]
    row0 = table.rows[0]
    row0.cells[0].text = "From Tutor Base to Period 1"
    row1 = table.rows[1]
    row1.cells[0].text = "From Period 1 to Period 2"
    row2 = table.rows[2]
    row2.cells[0].text = "From Period 2 to Period 3"
    row3 = table.rows[3]
    row3.cells[0].text = "From Period 3 to Period 4"
    row4 = table.rows[4]
    row4.cells[0].text = "From Period 4 to Period 5"
    row5 = table.rows[5]
    row5.cells[0].text = "From Period 5 to Period 6"

    rows = [row0, row1, row2, row3, row4, row5]
    rowIndex = 0
    columnIndex = 1
    position = 0
    fullRoute = ""
    
    while position != 5:
        temp = week[position]
        rowIndex = 0
        for route in temp:
            for room in route:
                fullRoute = fullRoute + room + "\n"
            fullRoute = fullRoute[:-1]
            rows[rowIndex].cells[columnIndex].text = fullRoute
            fullRoute = ""
            if rowIndex != 5:
                rowIndex+=1
            else:
                pass
        position +=1
        columnIndex +=1

    document.save('Timetable for ' + tutorGroup + '.docx')

    
        
app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
