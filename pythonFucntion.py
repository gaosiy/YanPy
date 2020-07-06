# property test
# using property to avoid change some unchangeable variable
class father():
    def __init__(self, dt=1, stim_amp=1, width=2, tstart=3):
        self._dt = dt
        self._stim_amp = stim_amp
        self._width = width
        self._tstart = tstart
        print('father init', self._dt)

    @property
    def stim_amp(self):
        return self._stim_amp

    @stim_amp.setter
    def stim_amp(self,x):
        self._stim_amp = x
        pass

