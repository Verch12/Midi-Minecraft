import mido
from mido import MidiFile


# Функция для расчета длительности MIDI трека
def calculate_midi_duration(midi_file_path):
    midi = MidiFile(midi_file_path)

    # Получаем темп из MIDI-файла
    tempo = 500000  # стандартный темп 120 BPM (в микросекундах на удар)

    # Начальные параметры
    ticks_per_beat = midi.ticks_per_beat
    duration_seconds = 0

    # Обрабатываем все сообщения в треке
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'set_tempo':
                tempo = msg.tempo  # обновляем темп, если находим событие "set_tempo"

            if msg.type == 'note_on' or msg.type == 'note_off':
                print(msg.channel)
            duration_seconds += msg.time/ ticks_per_beat * (tempo/ 1000000)

    # Преобразуем в минуты и секунды
    minutes = duration_seconds // 60
    seconds = duration_seconds % 60

    return minutes, seconds


# Пример использования
midi_file_path = '2.mid'  # Укажите путь к вашему MIDI файлу
minutes, seconds = calculate_midi_duration(midi_file_path)
print(f"Длительность MIDI трека: {int(minutes)} минут {int(seconds)} секунд")
