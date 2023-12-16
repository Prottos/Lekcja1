class Tank:
    def __init__(self, wariant, stan):
        self.variant = wariant
        self.ammo = 44
        self.condition = stan
        self.sight_mode_thermal = False
        self.detection_range = 4000
    
    def set_mode(self, mode):
        if mode == "thermal":
            self.sight_mode_thermal = True
            self.detection_range = 8000
        elif mode == "normal":
            self.sight_mode_thermal = False
            self.detection_range = 4000
        else:
            print("Brak zmian.")

