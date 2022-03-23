package classes.class_02_create_classes_and_objects;

public class Class02 {
  public static void main(String[] args) {
    Pen pen = new Pen();

    pen.model = "Bic";
    pen.color = "purple";
    pen.charge = 100;
    pen.nib = 0.7f;

    pen.uncover();
    pen.write();
    pen.status();
  }
}