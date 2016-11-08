# ApacheCon TAC Scripts

Some useful scripts to support [TAC](https://www.apache.org/travel/) organization at A[pacheCon](http://apachecon.com/).

Of course, all under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) ;-)

# Setup

```
pip install -r requirements.txt --upgrade
```

# Usage 

```
$ python3 ics2csv.py https://apachebigdataeu2016.sched.org/all.ics apachebigdataeu2016
tac Downloaded https://apachebigdataeu2016.sched.org/all.ics at apachebigdataeu2016.ics
tac Exported 128 talks to apachebigdataeu2016.csv
```

```
$ python3 ics2csv.py http://apacheconeu2016.sched.org/all.ics apachebigdataeu2016
tac Downloaded http://apacheconeu2016.sched.org/all.ics at apacheconeu2016.ics
tac Exported 124 talks to apacheconeu2016.csv
```
