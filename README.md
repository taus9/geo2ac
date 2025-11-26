
# geo2ac

This script takes the us-area-code-geo.csv located [here](https://github.com/ravisorg/Area-Code-Geolocation-Database/blob/master/us-area-code-geo.csv
) and uses the location data provided to retrieve the time zone that it's located in. Once it has done that it saves this data into a new CSV file.

It uses the free API key at [TimeZoneDB](https://timezonedb.com) which has a rate limit of one request per second which makes for a very slow process, but hey, it's free. Also the us-area-code-geo.csv file is very old, and at the time of writing this it is missing 73(?) new area codes.

Turns out I didn't need to do any of this. The North American Numerbing Plan Administrator provides this information. [NPA Reports](https://nanpa.com/reports/npa-reports)
