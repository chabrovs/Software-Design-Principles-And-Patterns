"""
This module implements the Facade pattern that easies \
the client interactions with the module classes.
"""


class FileLoader:
    def load(self, filename):
        return f"Loading file '{filename}'"


class VideoDecoder:
    def decode(self, file):
        return f"Decoding {file}"


class AudioExtractor:
    def extract_audio(self, file):
        return f"Extracting audio from {file}"


class VideoConverter:
    def convert(self, file, format):
        return f"Converting {file} to {format} format"


class VideoConvertedFacade:
    def __init__(self):
        self.loader = FileLoader()
        self.decoder = VideoDecoder()
        self.extractor = AudioExtractor()
        self.converter = VideoConverter()

    def convert_video(self, filename, format):
        file_ = self.loader.load(filename)
        decoded = self.decoder.decode(file_)
        audio = self.extractor.extract_audio(decoded)

        return self.converter.convert(file=audio, format=format), audio


# Client code
if __name__ == "__main__":
    facade = VideoConvertedFacade()
    video, audio = facade.convert_video("sample.mp4", "AVI")

    print(audio)
    print(video)
