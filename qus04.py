class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  
        self.inches = 0 
        self.on = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LEDTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"Brand: {self.brand}\nScreen Thickness: {self.screen_thickness} inches\nEnergy Usage: {self.energy_usage} watts\nLifespan: {self.lifespan} years\nRefresh Rate: {self.refresh_rate} Hz"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"Brand: {self.brand}\nScreen Thickness: {self.screen_thickness} inches\nEnergy Usage: {self.energy_usage} watts\nLifespan: {self.lifespan} years\nRefresh Rate: {self.refresh_rate} Hz"

led_tv = LEDTV("Sony", 1.2, 120, 5, 60)
print(led_tv.status())  # Displays TV status
print(led_tv.display_details())  # Displays TV details

