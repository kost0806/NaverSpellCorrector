from SpellCorrector import SpellCorrector
from ClipboardManager import ClipboardManager


if __name__ == '__main__':
    spell_corrector = SpellCorrector()
    while True:
        try:
            s = input('Correction: ')
        except KeyboardInterrupt:
            print('End Script')
            break

        if s.lower() == 'exit':
            print('End Script')
            break

        corrected_str = spell_corrector.correct(s)
        print('Corrected: ' + corrected_str.get_attribute('innerHTML'))
        ClipboardManager.set_clipboard(ClipboardManager.format_string(corrected_str.get_attribute('innerHTML')))
        print('Corrected result has been pasted in clipboard.')
