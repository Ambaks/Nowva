from datetime import datetime
class Set:
    def __init__(self, exercise , rep_count, length, rep_time_list, rep_velocity_list, plot):
        self.exercise = exercise
        self.rep_count = rep_count
        self.length = length
        self.rep_time = rep_time_list
        self.rep_velocity = rep_velocity_list
        self.plot = plot
        self.creation_time = datetime.now()

    def get_summary(self):
        return print(f'{self.exercise}: {self.rep_count} reps\nSet length: {self.length}s\nIndividual rep times: {self.rep_time}\nIndividual rep velocity: {self.rep_velocity}\nPlot{self.plot}\nCreation time: {self.creation_time}\n\n ')


