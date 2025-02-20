"""
This module implements the State design pattern. The state object are \
able to change the Context (Main Object)'s state dynamically.
"""


from abc import ABC, abstractmethod


class VideoPlayerState(ABC):
    """
    This class represents the 'State Interface (or Abstract State)'
    """

    @abstractmethod
    def press_play(self):
        ...


class PlayingState(VideoPlayerState):
    """
    this class represents a 'concrete state'
    """

    def press_play(self, player):
        print("⏸ pausing the media...")
        player.set_state(PausedState())


class PausedState(VideoPlayerState):
    """
    This class represents a 'Concrete State'
    """

    def press_play(self, player):
        print("▶ Resuming playback...")
        player.set_state(PlayingState())


class Player:
    """
    This class represents the 'Context (Main Object)'
    """

    def __init__(self):
        self._state = PausedState()  # Initial state.

    def set_state(self, state: VideoPlayerState):
        self._state = state

    def press_play(self):
        self._state.press_play(self)


# Client code
if __name__ == "__main__":
    player = Player()
    player.press_play()
    player.press_play()
    player.press_play()
