from cmath import pi
import time
import math

# Ref: https://www.likecs.com/show-970443.html


class DateTime:
    Y = time.localtime().tm_year
    M = time.localtime().tm_mon
    D = time.localtime().tm_mday
    h = time.localtime().tm_hour
    m = time.localtime().tm_min
    s = time.localtime().tm_sec


class SunTime:

    def __init__(self, sunrise, sunset):
        self.sunrise = sunrise
        self.sunset = sunset


class SunCalculator:

    def __init__(self, year, mon, day, lat, lon):
        self.year = year
        self.mon = mon
        self.day = day
        self.lat = lat
        self.lon = lon

    def getSunTimes(self) -> SunTime:
        st = SunTime(self.__calculate(True), self.__calculate(False))
        return st  # float

    def __calculate(self, calSunrise=True):

        zenith = 90.833333

        # 1. first calculate the day of the year
        N1 = math.floor(275 * self.mon / 9)
        N2 = math.floor((self.mon + 9) / 12)
        N3 = (1 + math.floor(
            (self.year - 4 * math.floor(self.year / 4) + 2) / 3))
        N = N1 - (N2 * N3) + self.day - 30
        # print("Day of year is:" + str(N))

        localOffset = math.floor(-1 * self.lon * 24 / 360)
        # print("Local offset is:" + str(localOffset))

        # 2. convert the longitude to hour value and calculate an approximate time
        lngHour = self.lon / 15
        if (calSunrise):
            t = N + ((6 - lngHour) / 24)  # sunrise
        else:
            t = N + ((18 - lngHour) / 24)  # sunset
        # print("Longitude hour is:" + str(lngHour))
        # print("t time is:" + str(t))

        # 3. calculate the Sun\'s mean anomaly
        M = (0.9856 * t) - 3.289
        # print("Mean anomaly is:" + str(M))

        # 4. calculate the Sun\'s true
        L = M + (1.916 * math.sin(M * pi / 180)) + (
            0.020 * math.sin(2 * M * pi / 180)) + 282.634
        # print("L is:" + str(L))
        L = (L + 360) % 360  # range of L is [0, 360)
        # print("L - 360 is:" + str(L))

        # 5.1 calculate the Sun\'s right ascension
        RA = (180 / pi) * math.atan(0.91764 * math.tan(L * pi / 180))
        RA = (RA + 360) % 360  # range of RA is [0, 360)
        # print("RA is:" + str(RA))

        # 5.2 right ascension value needs to be in the same quadrant as L
        Lquadrant = math.floor(L / 90) * 90
        Rquadrant = math.floor(RA / 90) * 90
        RA = RA + (Lquadrant - Rquadrant)

        # 5.3 right ascension value needs to be converted into hours
        RA = RA / 15

        # 6. calculate the Sun\'s declination
        sinDec = 0.39782 * math.sin(L * pi / 180)
        cosDec = math.cos(math.asin(sinDec))

        # 7.1 calculate the Sun\'s local hour angle
        cosH = (math.cos(zenith * pi / 180) -
                (sinDec * math.sin(self.lat * pi / 180))) / (
                    cosDec * math.cos(self.lat * pi / 180))
        # print("cosH is:" + str(cosH))
        if (cosH < -1):
            print(
                "the sun never sets on this location (on the specified date)")

        if (cosH > 1):
            print(
                "the sun never rises on this location (on the specified date)")

        # 7.2 finish calculating H and convert into hours
        if (calSunrise):
            H = 360 - 180 / pi * math.acos(cosH)  # sunrise
        else:
            H = 180 / pi * math.acos(cosH)  # sunset
        # print("H is:" + str(H))
        H = H / 15
        # print("H / 15 is:" + str(H))

        # 8. calculate local mean time of rising/setting
        T = H + RA - (0.06571 * t) - 6.622
        # print("T is:" + str(T))

        # 9. adjust back to UTC
        UTC = T - lngHour
        UTC = (UTC + 24) % 24  # range of UTC is [0, 24)
        # print("UT is:" + str(UTC))

        # 10. convert UT value to local time zone of latitude/longitude
        sunT = UTC - localOffset
        sunT = (sunT + 24) % 24
        # print("sunT is:" + str(sunT))

        return sunT


# for test

# def main():
#     dt = DateTime()
#     sunCalculator = SunCalculator(dt.Y, dt.M, dt.D, 39.92, 116.46)
#     sun = sunCalculator.getSunTimes()
#     print("sun.sunrise is:" + str(sun.sunrise) + "; sun.sunset is:" + str(sun.sunset))

# if __name__ == "__main__":
#     main()