class Mp3player():
    format='MP3' #static variable
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0]
            self.format=format
            print("creating the instance")
            print(Mp3player)
        elif len(args)==2:
            self.name=args[1]
            self.size=args[0]
            print("creating the instance")
    def play_name(self):
        print(f"{self.name}.{self.format} is played")
    def stop_play(self):
        print(f"{self.name}.{self.format} is stopped")
    def __str__(self):
        return " "
song1=Mp3player('Vidai kodu engal nade')
print(song1)
print(song1)
song2=Mp3player('7MB','dass sam')
print(song2.size)
song1.play_name()
song1.format="WAV"
song2.play_name()

print(isinstance(song1,Mp3player))
