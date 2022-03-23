package classes.class_02_create_classes_and_objects;

public class Pen {
  String model;
  String color;
  float nib;
  int charge;
  boolean isCovered;

  void write() {
    if (this.isCovered)
      System.out.println("error: Can't write, it's covered.");
    else {
      this.charge -= 5;
      System.out.println("It's doodling. The charge is in " + this.charge + "%");
    }
  };

  void cover() {
    this.isCovered = true;
  };

  void uncover() {
    this.isCovered = false;
  };

  void status() {
    System.out.println("Model: " + this.model);
    System.out.println("The " + this.color + " pen");
    System.out.println("Nib: " + this.nib);
    System.out.println("Charge: " + this.charge + "%");
    System.out.println("Is covered? " + this.isCovered);
  };
}