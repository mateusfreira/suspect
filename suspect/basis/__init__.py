import numpy


def gaussian(time_axis, frequency, phase, fwhm):
    oscillatory_term = numpy.exp(2j * numpy.pi * (frequency * time_axis + phase))
    damping = numpy.exp(-time_axis ** 2 / 4 * numpy.pi ** 2 / numpy.log(2) * fwhm ** 2)
    fid = oscillatory_term * damping
    # normalise the fid so the peak has area 1
    return fid / len(time_axis)


def lorentzian(time_axis, frequency, phase, fwhm):
    oscillatory_term = numpy.exp(1j * (2 * numpy.pi * frequency * time_axis + phase))
    damping = numpy.exp(-time_axis * numpy.pi * fwhm)
    fid = oscillatory_term * damping
    return fid / len(time_axis)
