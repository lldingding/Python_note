class MusicPlayer(object):
    instance = None
    init_flag = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return  cls.instance
    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print("working on")
        MusicPlayer.init_flag = True
qq = MusicPlayer()
print(qq)
wyy = MusicPlayer()
print(wyy)