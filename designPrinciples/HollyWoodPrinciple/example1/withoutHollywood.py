# In this example the App class controls the flow.

class PaymentProcessor:
    def process(self, amount):
        print(f"Processing payment for ${amount}")


class App:
    def start(self):
        processor = PaymentProcessor()
        processor.process(100)



if __name__ == "__main__":
    app = App()
    app.start()