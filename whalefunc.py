import vapoursynth as vs
import mvsfunc as mvf
import math
core = vs.get_core()
def solarcurve(clip):
    clip=mvf.ToRGB(clip)
    pi=3.1415926
    t = 3.2
    k = 3
    A = -1/4194304*(k*pi - 128/t)
    B = 3/32768*(k*pi - 128/t)
    C = 1/t

    def curveR(x):
        a=round(127.9999*math.sin(A*(x)**3 + B*(x)**2 + C**(x) ) + 127.5)
        return a
    def curveG(x):
        a=round(127.9999*math.sin(A*(x-5)**3 + B*(x-5)**2 + C**(x-5)) + 127.5)
        return a
    def curveB(x):
        a=round(127.9999*math.sin(A*(x+5)**3 + B*(x+5)**2 + C**(x+5)) + 127.5)
        return a
    clip = core.std.Lut(clip=clip, planes=[0], function=curveR)
    clip = core.std.Lut(clip=clip, planes=[1], function=curveG)
    clip = core.std.Lut(clip=clip, planes=[2], function=curveB)
    return clip