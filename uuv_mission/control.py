class controller:
    def __init__(self, KP=0.6, KD=0.45):
        # initialise the gains 
        self.KP = KP
        self.KD = KD
        # initialise previous error to 0 
        self.previous_error=0

    def position(self, reference, output):
        # Perform recurrence
        error = float(reference) - float(output)
        derivative = error - self.previous_error
        u = self.KP*error +self.KD*(derivative)
        self.previous_error = error
        return u 

