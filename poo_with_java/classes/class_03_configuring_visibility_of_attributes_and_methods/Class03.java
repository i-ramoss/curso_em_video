package classes.class_03_configuring_visibility_of_attributes_and_methods;

public class Class03 {
  public static void main(String[] args) {
    Pen pen = new Pen();

    pen.model = "Faber Castel";
    pen.color = "white";
    // pen.nib = 0.7; // The field Pen.nib is not visible (private)
    pen.charge = 80;
    pen.isCovered = true;
  }
}