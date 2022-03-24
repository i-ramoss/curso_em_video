package exercises.class02;

public class Cabinet {
  String model;
  String brand;
  String color;
  String motherboard;
  String processor;
  String graphicsCard;
  String font;
  String colorOfFans;

  int width;
  int height;
  int weight; 
  int ramMemorySize;
  int ssdSize;
  int hdSize;
  int numberOfFans;
  int numberOfUsbPorts;

  boolean isOn;
  boolean hasSsd;
  boolean hasHd;

  void powerOn() {
    this.isOn = true;
  }

  void getCabinetInformation() {
    System.out.println("Model: " + this.model);
    System.out.println("Brand: " + this.brand);
    System.out.println("Color: " + this.color);
    System.out.println("Motherboard: " + this.motherboard);
    System.out.println("Processor: " + this.processor);
    System.out.println("Graphic card: " + this.graphicsCard);
    System.out.println("Font: " + this.font);
    System.out.println("Color of fans: " + this.colorOfFans);
    System.out.println("Height " + this.height);
    System.out.println("Width " + this.width);
    System.out.println("Weight " + this.weight);
    System.out.println("Ram memory size " + this.ramMemorySize);
    System.out.println("SSD size " + this.ssdSize);
    System.out.println("HD size " + this.hdSize);
    System.out.println("Number of fans " + this.numberOfFans);
    System.out.println("Number of usb ports " + this.numberOfUsbPorts);
  }
}
