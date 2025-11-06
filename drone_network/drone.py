class GenesisDrone:
    def __init__(self):
        self.starters = ["Juice", "Kick", "Seed", "Spark", "Flex"]

    def create_proto_drone(self):
        return ProtoDrone(self.starters[:])


class ProtoDrone:
    def __init__(self, received_starters):
        self.starters = received_starters

    def receive_starter(self, starter):
        self.starters.append(starter)
