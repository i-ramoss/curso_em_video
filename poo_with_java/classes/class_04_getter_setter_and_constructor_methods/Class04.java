package classes.class_04_getter_setter_and_constructor_methods;

public class Class04 {
  public static void main(String[] args) {
    Pen pen = new Pen("Faber Castel", "black", 0.2f);
    Pen pen2 = new Pen("Positive", "blue", 1.0f);

    pen.status(); // Return the initial pen values, instantiate on constructor

    System.out.println("\n------------------\n");

    pen2.status();

    // pen.model = "Crystal BIC"; // Accessing a private attribute directly results
    // in a error
    pen.setModel("Crystal BIC"); // Use the setter method to modify the private value

    // pen.nib = 0.5; // Accessing a private attribute directly results in a error
    pen.setNib(0.5f); // Use the setter method to modify the private attribute

    System.out.println("\n------------------\n");

    pen.status();
  }
}