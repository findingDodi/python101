import time


class BasicClass:
    __instance_counter = 0

    def __init__(self, new_label="default"):
        BasicClass.__instance_counter += 1
        self.label = new_label
        self.logged_time = 0.0

    def set_label(self, new_label):
        self.label = new_label

    def get_info(self):
        return "Label: '{}', Time: '{}', Counter: '{}'".format(
            self.label, self.logged_time, BasicClass.__instance_counter)

    def log_time(self):
        self.logged_time = time.time()

    def __del__(self):
        print("{} has been killed!".format(self.label))
        BasicClass.__instance_counter -= 1
