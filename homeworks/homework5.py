from abc import ABC, abstractmethod


class File(ABC):
    @abstractmethod
    def open(self):
        pass

@abstractmethod
def get_info(self):
    pass


class TextFile(File):
    def open(self):
        print("Открываем текстовый файл...")
        print("Привет! Это содержимое текстового файла.")

    def get_info(self):
        print("Информация: текстовый файл (.txt)")


class ImageFile(File):
    def open(self):
        print("Открываем изображение...")
        print(r"""
  /\_/\
 ( o.o )
  > ^ <
        """)

    def get_info(self):
        print("Информация: изображение (.png)")


class AudioFile(File):
    def open(self):
        print("Воспроизводим аудиофайл...")

    def get_info(self):
        print("Информация: аудиофайл (.mp3)")


class VideoFile(File):
    def open(self):
        print("Воспроизводим видеофайл...")

    def get_info(self):
        print("Информация: видеофайл (.mp4)")


files = [
    TextFile(),
    ImageFile(),
    AudioFile(),
    VideoFile()
]

for file in files:
    file.open()
    file.get_info()
    print()
