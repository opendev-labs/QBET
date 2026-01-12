class REPL:
    def __init__(self):
        self.version = "1.0.0"

    def run(self):
        print(f"QBET {self.version} REPL")
        print("Type 'exit' or Ctrl+D to leave.")
        try:
            while True:
                line = input("qbet> ")
                if not line or line.lower() == 'exit':
                    break
                print(f"Intention captured: {line}")
                print("🌀 Collapsing...")
        except EOFError:
            print("\nLeaving the field.")
