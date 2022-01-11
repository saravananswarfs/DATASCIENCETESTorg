class Mp3player():
    format='MP3' #static variable
    def __init__(self,size,name):
        self.size=size
        self.name=name
    def play_name(self):
        print(f"{self.name}.{self.format} is played")
    def stop_play(self):
        print(f"{self.name}.{self.format} is stopped")
    def __str__(self):
        return " "
song1=Mp3player('3MB','Vidai kodu engal nade')
print(song1)
song2=Mp3player('7MB','dass sam')
print(song2)
song1.play_name()
song1.format="WAV"
song2.play_name()

print(isinstance(song1,Mp3player))
