package classes.class_03_configuring_visibility_of_attributes_and_methods;

public class Pen {
  public String model;
  public String color;
  private float nib;
  protected int charge;
  protected boolean isCovered;

  public void write() {
    if (this.isCovered)
      System.out.println("error: Can't write, it's covered.");
    else {
      this.charge -= 5;
      System.out.println("It's doodling. The charge is in " + this.charge + "%");
    }
  }

  protected void cover() {
    this.isCovered = true;
  }

  protected void uncover() {
    this.isCovered = false;
  }

  public void status() {
    System.out.println("Model: " + this.model);
    System.out.println("The " + this.color + " pen");
    System.out.println("Nib: " + this.nib);
    System.out.println("Charge: " + this.charge + "%");
    System.out.println("Is covered? " + this.isCovered);
  }
}