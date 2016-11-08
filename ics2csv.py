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
import csv


def ics2csv(ics):
    """
    Transforms a ICS files to CSV

    ics: ics path or url
    """
    logging.basicConfig(level=logging.DEBUG, format="\033[1m%(name)s\033[0m %(message)s")
    logging.getLogger("requests").setLevel(logging.WARNING)
    log = logging.getLogger("tac")

    if ics.startswith("http") or ics.startswith("http"):
        url = ics
        ics = download_file(url)
        log.debug("Downloaded %s at %s", url, ics)

    slots = []
    with open(ics, 'r') as g:
        gcal = Calendar.from_ical(g.read())
        for component in gcal.walk():
            if component.name == "VEVENT":
                title = component.get('summary')
                time = component.get('dtstart').dt.strftime("%Y-%m-%d %H:%M")
                location = re.sub(', Seville, Spain$', '', component.get('location'))
                slots.append((title, location, time))

    csv_path = "%s.csv" % splitext(basename(ics))[0]
    with open(csv_path, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["talk", "room", "time", "volunteer", "backup"])
        for slot in slots:
            writer.writerow(slot)
    log.info("Exported %d talks to %s", len(slots), csv_path)


if __name__ == "__main__":
    run(ics2csv)