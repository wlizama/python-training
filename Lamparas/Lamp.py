
class Lamp:

    _LAMPS = ['''
          .
     .    |    .
      \   '   /
       ' .-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
              '''



         .-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    # Método contrucctor
    def __init__(self, _is_turn_on):
        self._is_turn_on = _is_turn_on
        self._display_image()

    def turnOff(self):
        self._is_turn_on = False
        self._display_image()

    def turnOn(self):
        self._is_turn_on = True
        self._display_image()

    def _display_image(self):
        if self._is_turn_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
