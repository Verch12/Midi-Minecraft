from InstrType import ID
import mido


class MidiConverter:
    def __init__(self, file_name):
        self.fileName = file_name
        self.instrumentID = ID()

        self.command = []

        self.instrument = []
        self.instrumentMine = []
        self.channel = set()

        self.note = {}

    def convert(self):
        midi = mido.MidiFile(self.fileName)

        for track in midi.tracks:
            for msg in track:
                self.command.append(msg)

    def instrumentConverterType(self):
        channel_instruments = {}

        for msg in self.command:
            if msg.type == 'program_change':
                channel_instruments[msg.channel] = msg.program

            if msg.type == 'note_on' or msg.type == 'note_off':
                self.channel.add(msg.channel)

        for i in self.channel:
            instrument = channel_instruments.get(i, 'Unknown')
            try:
                self.instrumentMine.append(self.instrumentID[instrument + 1])
                self.instrument.append(instrument)
            except KeyError:
                self.instrumentMine.append(self.instrumentID[4])
                self.instrument.append(4)
            except TypeError:
                self.instrumentMine.append(self.instrumentID[4])
                self.instrument.append(4)

        # print(self.instrumentMine)
        # print(self.instrument)
        # print(self.channel)

    def noteConvert(self):
        note_instruments = []
        channels = set()

        for msg in self.command:
            if msg.type == 'note_on' or msg.type == 'note_off':
                channels.add(msg.channel)
                note_instruments.append([msg.note, msg.channel])

        for i in channels:
            self.note[i] = []

        for i in note_instruments:
            if i[0] // 12 <= 4:
                self.note[i[1]].append(i[0] % 12 + 1)
            if i[0] // 12 >= 5:
                self.note[i[1]].append(i[0] % 12 + 13)

        # return self.note.get(0, None)


Converter = MidiConverter("..\\MidiFiles\\123.mid")
Converter.convert()
Converter.instrumentConverterType()

print(Converter.noteConvert())
