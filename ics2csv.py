#!/usr/bin/python
# -*- coding: utf8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from clize import run
from utils import download_file
import re
from os.path import basename, splitext
from icalendar import Calendar
import datetime
import pytz
import csv


stopwords = [
    "breakfast",
    "registration",
    "sponsor showcase",
    "coffee break",
    "lunch"
    "barcamp",
    "keynote",
    "morning run",
    "attendee reception"
    "BarCampApache"
]


def ics2csv(ics, name=None):
    """
    Transforms a ICS files to CSV

    ics: ics path or url

    name: conference name (optional)
    """

    logging.basicConfig(level=logging.DEBUG, format="\033[1m%(name)s\033[0m %(message)s")
    logging.getLogger("requests").setLevel(logging.WARNING)
    log = logging.getLogger("tac")

    if name is None:
        name = splitext(basename(ics))[0]

    csv_path = "%s.csv" % name
    ics_path = "%s.ics" % name

    if ics.startswith("http") or ics.startswith("http"):
        ics_path = download_file(ics, ics_path)
        log.debug("Downloaded %s at %s", ics, ics_path)

    slots = []
    with open(ics_path, 'r') as g:
        gcal = Calendar.from_ical(g.read())
        for component in gcal.walk():
            if component.name == "VEVENT":
                title = component.get('summary')
                start_time_utc = component.get('dtstart').dt
                local_tz = pytz.timezone('US/Eastern')  # TODO: arg
                start_time_local = start_time_utc.astimezone(local_tz)
                start = start_time_local.strftime("%Y-%m-%d %H:%M")
                location = re.sub(', Miami, FL, United States$', '', component.get('location'))   # TODO: arg

                if not any(stopword in title.lower() for stopword in stopwords):
                    slots.append((title, location, start))

    with open(csv_path, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        #writer.writerow(["talk", "room", "time", "volunteer", "backup"])
        for slot in slots:
            writer.writerow(slot)
    log.info("Exported %d talks to %s", len(slots), csv_path)


if __name__ == "__main__":
    run(ics2csv)
