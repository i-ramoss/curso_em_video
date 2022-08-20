package classes.class_04_getter_setter_and_constructor_methods;

public class Pen {
  private String model;
  private String color;
  private float nib;
  private boolean isCovered;

  public String getModel() {
    return this.model;
  }

  public void setModel(String model) {
    this.model = model;
  }

  public String getColor() {
    return this.color;
  }

  public void setColor(String color) {
    this.color = color;
  }

  public float getNib() {
    return this.nib;
  }

  public void setNib(float nib) {
    this.nib = nib;
  }

  public boolean getIsCovered() {
    return this.isCovered;
  }

  public void setIsCovered() {
    this.isCovered = true;
  }

  public void setIsNotCovered() {
    this.isCovered = false;
  }

  public void status() {
    System.out.println("Model: " + this.getModel());
    System.out.println("Nib: " + this.getNib());
    System.out.println("Color: " + this.getColor());
    System.out.println("Is covered : " + this.getIsCovered());
  }
}