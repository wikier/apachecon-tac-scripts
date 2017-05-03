# ApacheCon TAC Scripts

Some useful scripts to support [TAC](https://www.apache.org/travel/) organization at [ApacheCon](http://apachecon.com/).

Of course, all under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) ;-)

# Setup

```
pip install -r requirements.txt --upgrade
```

# Usage 

```
$ python3 ics2csv.py https://apachebigdata2017.sched.org/all.ics apachebigdata2017
tac Downloaded https://apachebigdata2017.sched.org/all.ics at apachebigdata2017.ics
tac Exported 88 talks to apachebigdata2017.csv
```

```
$ python3 ics2csv.py https://apachecon2017.sched.com/all.ics apachecon2017
tac Downloaded https://apachecon2017.sched.com/all.ics at apachecon2017.ics
tac Exported 124 talks to apachecon2017.csv
```
