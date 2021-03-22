# На наклонной плоскости с углом наклона 13° находится тело, прикрепленное к нити,
# перекинутой через блок, а к другому концу нити прикреплено второе тело,
# висящее вертикально. Коэффициент трения между первым телом и плоскостью 0,07.
# Найти отношение масс второго тела к первому, при котором второе тело начнет подниматься.
# Трения в блоке нет.
import math

mu = 0.07
alfa = 13
print(f'm2/m1 < {round(math.sin(math.radians(alfa) - mu), 3)}')