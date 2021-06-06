"""
  Project: Homework 13.2
  Author: 최민수
  StudentID: 21511796
  Date of last update: June. 7, 2021
  Detail: 전자 피아노를 구현하고, 자동 음악 연주 기능을 추가.
"""
import pyaudio
import numpy as np

lower_cases = \
    [262, 196, 165, 330, 659, 349, 392, 440, 1046, 494,
    # a(C4), b, c, d, e, f, g, h, i, j,
    523, -1, 247, 220, -1, -1, 523, 698, 294, 784,
    # k, l, m, n, o, p, q(C5), r, s, t,
    988, 175, 587, 147, 880, 131]
    # u, v, w, x, y, z (C3)
upper_cases = \
    [2093, 1568, 1318, 2637, 5274, 2794, 3136, 3520, -1, 3951,
    # A(C7), B, C, D, E, F, G, H, I, J,
    4186, -1, 1975, 1760, -1, -1, 4186, 5587, 2349, 6272,
    # K, L, M, N, O, P, Q(C8), R, S, T,
    7902, 1397, 4969, 1175, 7040, 1046]
    # U, V, W, X, Y, Z(C6)

def pyaudio_init():
    global pa, stream
    volume=.5
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paFloat32, channels=1, rate=48000, output=True)
def pyaudio_play(freq, duration, volume):
    global pa, stream
    rate=48000
    sample = (np.sin(2*np.pi *\
    np.arange(rate * duration)*freq/rate)).astype(np.float32)
    stream.write(volume * sample)
def pyaudio_close():
    global pa, stream
    stream.stop_stream()
    stream.close()
    pa.terminate()

def sheetevent(note, play_time):
    note = ord(note)
    if (ord('a') <= note <= ord('z')):
        freq = lower_cases[note - ord('a')]
    elif(ord('A') <= note <= ord('Z')):
        freq = upper_cases[note - ord('A')]
    else:
        return
    if freq > 40:
        pyaudio_play(freq, play_time*2, 0.5)
    

def playingSheet(sheet_music):
    for t in sheet_music:
        note, play_time = t[0], t[1]
        sheetevent(note, play_time)

def main():
    sheet_music = (('g',1),('q',1),('j',0.5),('q',0.5),('w',1),('q', 0.5),('w',0.5),
    ('e',1),('r',0.5),('e',0.5),('h',1),('w',0.5),('w',0.5),('q',1),('q',0.5),('q',0.5),
    ('j',1),('h',0.5),('j',0.5),('q',1.5))
    pyaudio_init()
    playingSheet(sheet_music)
    pyaudio_close()
if __name__ == "__main__":
    main()