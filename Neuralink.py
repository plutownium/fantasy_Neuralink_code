class OperatingSystem:
    def __init__(self):
        pass


class Routine:
    def __init__(self, activity, schedule, duration, between_hours, limit_by_weather=False):
        self.activity = activity
        self.schedule = schedule
        self.duration = duration
        self.between_hours = between_hours
        self.weather = limit_by_weather

    def start(self):
        """Runs the activity for its duration unless interrupted."""
        # TODO: Fill me in!
        pass
