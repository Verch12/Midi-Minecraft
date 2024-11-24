import mido

midi = mido.MidiFile("123.mid")

tempo = 500000
ticks_per_beat = midi.ticks_per_beat
total_time = 0

for track in midi.tracks:
    track_time = 0
    for msg in track:
        if msg.type == 'set_tempo':
            tempo = msg.tempo

        track_time += msg.time/ ticks_per_beat * (tempo/ 1000000)
    total_time = max(total_time, track_time)

minutes = total_time // 60
seconds = total_time % 60

print(f"Длительность MIDI трека: {int(minutes)} минут {seconds:.2f} секунд")

#1 5:04