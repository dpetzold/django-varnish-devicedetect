class Device:

    def __init__(self, device_name):
        self.device_name = device_name
        setattr(self, device_name.replace('-', '_'), True)
        if '-' in device_name:
            device_type, device_model = device_name.split('-')
            setattr(self, 'is_{}'.format(device_type), True)
            setattr(self, 'is_{}'.format(device_model), True)
        else:
            setattr(self, 'is_{}'.format(device_name), True)

    def __str__(self):
        return self.device_name

    def __getattr__(self, name):
        return False
