# Livescore

## Description

Scrapy-based web scraper for live football(soccer) games. It returns the competition, time(GMT+2), status, home-team, score, and away-team.

Example

```
{"competition": "Italie : Serie A", "time": "19:00", "status": "47'", "home-team": "Naples", "score": "1 - 0", "away-team": "Rome"}
{"competition": "Angleterre : League Championship", "time": "18:30", "status": "78'", "home-team": "Bristol City", "score": "1 - 1", "away-team": "Sheffield United"}
{"competition": "Espagne : Liga Adelante", "time": "19:00", "status": "52'", "home-team": "Girona", "score": "0 - 0", "away-team": "Real Sociedad B"}
{"competition": "Turquie : S\u00fcper Lig", "time": "19:30", "status": "35'", "home-team": "Galatasaray", "score": "0 - 0", "away-team": "Yeni Malatyaspor"}
{"competition": "Angleterre : Conference National", "time": "18:20", "status": "90'", "home-team": "Halifax Town", "score": "2 - 0", "away-team": "Chesterfield"}
{"competition": "Angleterre : Premier League 2 Division One", "time": "20:00", "status": "8'", "home-team": "Leicester City U23", "score": "0 - 0", "away-team": "Blackburn Rovers U23"}
{"competition": "Angleterre : Premier League 2 Division Two", "time": "20:00", "status": "5'", "home-team": "Sunderland U23", "score": "0 - 0", "away-team": "Aston Villa U23"}
```

In the first line of the output, the game is in Italy for the Serie A, kick-off at 19:00, playing the 47th minute, Napoli(home-team) 1 - 0 AS Roma(away-team)

## Usage


```
$ git clone https://github.com/aissa-laribi/livescore.git
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install scrapy
$ scrapy runspider main.py -s FEED_EXPORT_ENCODING=utf8 -O output.jl
```
