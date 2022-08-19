package classes.class_04_getter_setter_and_constructor_methods;

public class Pen {
  private String model;
  private float nib;

  public String getModel() {
    return this.model;
  }

  public void setModel(String model) {
    this.model = model;
  }

  public float getNib() {
    return this.nib;
  }

  public void setNib(float nib) {
    this.nib = nib;
  }

  public void status() {
    System.out.println("Model: " + this.model);
    System.out.println("Nib: " + this.nib);
  }
}