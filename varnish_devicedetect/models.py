class Device:

    def __init__(self, device_name):
        self.device_name = device_name
        setattr(self, device_name.replace('-', '_'), True)

    def __str__(self):
        return self.device_name

    def __getattr__(self):
        return False
