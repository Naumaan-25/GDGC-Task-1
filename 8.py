class Model:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def train(self):
        print(f"Training {self.name} model...")

my_ai = Model("GPT-4", "LLM")
my_ai.train()