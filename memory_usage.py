import logging


class MemoryUsage:
    def __init__(self, memory, percentage_amount):
        self.memory = memory
        self.percentage_amount = percentage_amount

    def create_dictionary(self):
        dict = {
            "Total Memory:": self.memory.total,
            "Free Memory:": self.memory.available,
            "Memory Used:": self.memory.used,
        }
        return dict

    def over_threshold(self):
        if self.memory.percent > self.percentage_amount:
            file_name = "memory.log"
            logging.basicConfig(filename=file_name, filemode="w", level=logging.INFO)
            logging.info("Monitoring the overall memory usage of the system:")
            dictionary = self.create_dictionary()
            logging.info(dictionary)
        else:
            print("Nothing to log at the moment.")
