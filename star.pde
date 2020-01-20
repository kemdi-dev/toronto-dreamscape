color c = color(0);
float x = 0;
float y = 100;
float speed = 1;

void moveRight() {
  x = x + speed;
  if (x > width) {
    x = 0;
  }
}

void ascend () {
  y--;
  x = x + random (-2, 2);
}

void star(float x, float y, float radius1, float radius2, int npoints) {
  
  float angle = TWO_PI / npoints;
  
  float halfAngle = angle/5.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += (angle = TWO_PI / npoints)) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;

    // Generating random values for the ocean-like's coordinates.
    float rStar = random(-150, 150);
    vertex(sx+rStar, y); 
    //vertex(rStar, rStar); 
    //vertex(rStar, sy); 

    sx = x + cos(a + halfAngle) * radius1;
    sy = y + sin(a + halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}
