import mido

Instrument = {
    25: 'Шерсть',
    26: 'Шерсть',
    27: 'Шерсть',
    28: 'Шерсть',
    29: 'Шерсть',
    34: 'Доски',
    35: 'Доски',
    36: 'Доски',
    35: 'Каменный',
    36: 'Каменный',
    38: 'Песчаный',
    40: 'Песчаный',
    116: 'Стеклянный',
    14: 'Костяной блок',
    113: 'Плотный лёд',
    15: 'Золотой блок',
    12: 'Железый блок',
    73: 'Глина',
    74: 'Глина',
    76: 'Глина',
    -1: 'Песок душ',
    21: 'Изумрудный блок',
    106: 'Сноп сена',
    5: 'Светокамень',
    6: 'Светокамень',
    47: 'Другие блоки',
    4: 'Другие блоки',
}

def ticks_to_seconds(ticks, tempo, ppqn):
    seconds_per_beat = 60 / tempo
    seconds_per_tick = seconds_per_beat / ppqn
    return ticks * seconds_per_tick

mid = mido.MidiFile("..\\MidiFiles\\123.mid")
channel_instruments = {}

ppqn = mid.ticks_per_beat   # Количество тиков на четвертную ноту (PPQN)

length_in_seconds = 0

for i, track in enumerate(mid.tracks):
    for msg in track:
        if msg.type == 'program_change':
            # Сохраняем активный инструмент для текущего канала
            channel_instruments[msg.channel] = msg.program

        if msg.type == 'set_tempo':
            # Выводим темп (в микросекундах на такт)
            tempo = msg.tempo

        if msg.type == 'note_on' or msg.type == 'note_off':
            # Получаем инструмент для канала, на котором произошла нота
            instrument = channel_instruments.get(msg.channel, 'Unknown')
            instr = ''

            if msg.note // 12 <= 4:
                Note = msg.note % 12 + 1
            if msg.note // 12 >= 5:
                Note = msg.note % 12 + 13

            try: instr = Instrument[instrument+1]
            except KeyError: instr = Instrument[4]
            except TypeError: instr = Instrument[4]

            print(f'Note: {Note}, Time: {msg.time}, Instrument: {instr}, {instrument}')
print("aaf", length_in_seconds)