/*
DATT 3935: 
  Data Art Project
Group Members:
  Kemdi Ikejiani
  Vivien Hung
  Tran Pham
References:
  https://www.processing.org/tutorials/objects/
*/

String utDataFile = "UTconstructionDetails.csv";
String demolDataFile = "demolDets2015-2018.csv";

ArrayList <NewBuild> newProjects = new ArrayList();
ArrayList <DemolBuild> demolished = new ArrayList();

float r;
float g;
float b;
Float a;

PImage sunset;
PImage bg;
PImage tower;

int maxStorey = 0;

void setup() {
  
  size(1000,800);
  
  // Load images
  sunset = loadImage("sunset.jpg");
  bg = loadImage("bg_2.jpg");
  tower = loadImage("tower-w.png");

  //Load Urban Toronto Construction CSV
  Table constructionCSV = loadTable(utDataFile, "header, csv");
  for (TableRow constructionRow : constructionCSV.rows()) {
    NewBuild newBuilding = new NewBuild();
    
    newBuilding.title = constructionRow.getString("Title");
    newBuilding.lat = constructionRow.getFloat("Latitude");
    newBuilding.lng = constructionRow.getFloat("Longitude");
    newBuilding.address = constructionRow.getString("Address");
    newBuilding.category = split(constructionRow.getString("Category"), ',');
    newBuilding.status = constructionRow.getString("Status");
    newBuilding.comDate = constructionRow.getInt("Completion Date");
    newBuilding.storey = constructionRow.getInt("Storeys");
    newBuilding.heightFT = constructionRow.getInt("Height in ft");
    
    newProjects.add(newBuilding); 
    maxStorey = max(maxStorey, newBuilding.storey);
  }
  
  Table demolishedCSV = loadTable(demolDataFile, "header, csv");
  for (TableRow demolRow : demolishedCSV.rows()) {
    DemolBuild demolBuilding = new DemolBuild();
    
    demolBuilding.address = demolRow.getString("Address");
    demolBuilding.lat = demolRow.getFloat("Latitude");
    demolBuilding.lng = demolRow.getFloat("Longitude");
    String[] date = split(demolRow.getString("Completion Date"), '-');
    demolBuilding.year = int(date[0]);
    demolBuilding.month = int(date[1]);
    
    demolished.add(demolBuilding);
  }
}

void draw() {
  
  background(8,70,163);
  frameRate (30);
  sunset.resize(width, 500);
  image(bg,0,0);
  // image(sunset, 0, 0);  
  
  fill(0, 100);
  //rect(0, 0, width, height);
  
  for (NewBuild buildings : newProjects) {
    
    noStroke();
    
    Float xpos = map(buildings.lng, -79.594317, -79.1843517, 0, width);
    float ypos = map(buildings.storey, 0, 147, 490, 0); // Map to lowest (300) to highest (0) of window.
    
    // Make sure to subtract the mapped storey height with the pixels above to create line.
    noStroke();
    
    a = map(buildings.comDate, 0, 2022, 50, 200);
    
    if (buildings.status.equals("Complete")) {
      r = 248;
      g = 44;
      b = 101;
      //a = 200.0;
      stroke(255, 180);
      strokeWeight(1);
    } else if (buildings.status.equals("Under Construction")) {
      r = 47;
      g = 143;
      b = 174;
    } else {
      //stroke(27, 174, 134, 200);
      //stroke(255, a + 20);
      strokeWeight(1);
      r = 80;
      g = 80;
      b = 80;
      //a = 0.0;
    }
    
    fill(r, g, b, a);
    rect(xpos, ypos, 25, (500 - ypos));
    
  }
  for (DemolBuild demol : demolished) {
    
    noStroke();
    
    Float xpos = map(demol.lng, -79.594317, -79.1843517, 0, width);
    int yearScale = int(map(demol.year, 2015, 2018, 0,3)*12);
    int dateScale = yearScale + demol.month;
    float ypos = map(dateScale, 1, 48, height - 10, 500); 
    
    fill(255, 255, 255, 5); 
    star(xpos, ypos, 20, 20, 10); 
    fill(0, 255, 255, 5); 
    star(xpos, ypos, 20, 20, 10); 
    fill(0, 0, 255, 5); 
    star(xpos, ypos, 20, 20, 10); 
    fill(102, 255, 178, 5); 
    star(xpos, ypos, 20, 20, 10);
  }
  
  tower.resize(0,490);
  Float xpos = map(-79.3871, -79.594317, -79.1843517, 0, width);
  
  image(tower, xpos - 45, 10); 
}
