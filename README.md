# ApacheCon TAC Scripts

Some useful scripts to support [TAC](https://www.apache.org/travel/) organization at [ApacheCon](http://apachecon.com/).

Of course, all under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) ;-)

# Setup

```
pip install -r requirements.txt --upgrade
```

# Usage 

```
$ python3 ics2csv.py https://apachebigdata2017.sched.org/all.ics apachebigdataeu2017
tac Downloaded https://apachebigdata2017.sched.org/all.ics at apachebigdataeu2017.ics
tac Exported 88 talks to apachebigdataeu2017.csv
```

```
$ python3 ics2csv.py https://apachecon2017.sched.com/all.ics apacheconeu2017
tac Downloaded https://apachecon2017.sched.com/all.ics at apacheconeu2017.ics
tac Exported 124 talks to apacheconeu2017.csv
```
