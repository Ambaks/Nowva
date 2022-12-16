class Set:
    def __init__(self, exercise , rep_count, length, rep_time_list, rep_velocity_list, plot):
        self.exercise = exercise
        self.rep_count = rep_count
        self.length = length
        self.rep_time = rep_time_list
        self.rep_velocity = rep_velocity_list
        self.plot = plot

squat = Set('Squat', 5, 5, [1,1,1,1,1], [1,1,1,1,1], 0)
print(squat.rep_velocity)
