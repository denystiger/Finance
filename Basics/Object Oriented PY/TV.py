class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channel_list = [0, 1, 4, 9, 12, 42, 50, 90]
        self.n_channels = len(self.channel_list)
        self.chan_idx = 0
        self.vol_min = 0
        self.vol_max = 10
        self.vol = 5

    def power(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted=False
        if self.vol < self.vol_max:
            self.vol +=1
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted= False
        if self.vol > self.vol_min:
            self.vol -= 1
    def channelUp(self):
        if not self.isOn:
            return
        self.chan_idx += 1
        if self.chan_idx > self.n_channels:
            self.chan_idx = 0
    def channelDown(self):
        if not self.isOn:
            return
        self.chan_idx -= 1
        if self.can_idx < 0:
            self.chan_idx = self.n_channels - 1
    def mute(self):
        self.isMuted = not self.isMuted
    def set_Channel(self, new_channel):
        if new_channel in self.channel_list:
            self.chan_idx = self.channel_list.index(new_channel)
    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('    TV is: ON')
            print('    Channel is ', self.channel_list[self.chan_idx])
            if self.isMuted:
                print('     Volume is', self.vol, 'sound is muted')
            else:
                print('      Volume is', self.vol)
        else:
            print('    TV is: Off')
