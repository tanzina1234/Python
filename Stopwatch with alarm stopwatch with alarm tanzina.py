import time
import threading

class Stopwatch:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.alarm_time = None

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started.")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print("Stopwatch stopped.")

    def reset(self):
        self.elapsed_time = 0
        self.start_time = None
        self.running = False
        print("Stopwatch reset.")

    def show_time(self):
        if self.running:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time
        minutes, seconds = divmod(current_time, 60)
        print(f"Elapsed Time: {int(minutes):02}:{int(seconds):02}")

    def set_alarm(self, duration):
        self.alarm_time = duration
        print(f"Alarm set for {duration} seconds.")
        threading.Thread(target=self._alarm_countdown).start()

    def _alarm_countdown(self):
        time.sleep(self.alarm_time)
        print("\n*** Alarm! Time's up! ***")
        self.alarm_time = None


def main():
    stopwatch = Stopwatch()

    while True:
        print("\nOptions: start, stop, reset, show, alarm, exit")
        choice = input("Enter your choice: ").lower()

        if choice == "start":
            stopwatch.start()
        elif choice == "stop":
            stopwatch.stop()
        elif choice == "reset":
            stopwatch.reset()
        elif choice == "show":
            stopwatch.show_time()
        elif choice == "alarm":
            try:
                duration = int(input("Enter alarm duration in seconds: "))
                stopwatch.set_alarm(duration)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "exit":
            print("Exiting stopwatch. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()