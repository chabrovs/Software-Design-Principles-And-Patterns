"""
This module does not implement the Facade pattern \
and the client need to know all the implementation details \
in order to work with this module efficiently.
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


# Client code

if __name__ == "__main__":
    loader = FileLoader()
    decoder = VideoDecoder()
    extractor = AudioExtractor()
    converter = VideoConverter()

    file_ = loader.load("sample.mp4")
    decoded = decoder.decode(file_)
    audio = extractor.extract_audio(decoded)
    converted = converter.convert(decoded, "AVI")

    print(audio)
    print(converted)
