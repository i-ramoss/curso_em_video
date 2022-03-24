package exercises.class02;

public class EchoDot {
  String color;
  int generation;
  int volume;
  boolean isActive;
  boolean isMute;

  void increaseVolume() {
    if (this.volume < 10)
      this.volume += 1;
  };

  void decreaseVolume() {
    if (this.volume > 0)
      this.volume -= 1;
  };

  void mute() {
    this.isMute = true;
  };

  void activate() {
    this.isActive = true;
  };
}
