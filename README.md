# Mulyrica

~~A tool for analyzing and providing useful insights into lyrics.~~
A tool for generating popular song lyrics.

```
Inputs: Song and Author + Tweets
Outputs: Sentiment analysis + Lyrics **Updated**
```

## Preliminaries

You might have to install the `vader_lexicon` package (Will fix this) to use the
`SentimentIntensityAnalyzer`.

Run this in `python shell` after activating venv` `nltk.download('vader_lexicon').`

## Setup

## Twitter integration

- Pending

### Frontend

- [ ] Bootstrap + JavaScript/jQuery

- [ ] ReactJS + CSS


### Activating your virtualenv

Create and activate a `python environment` outside your app.

Make sure to install `gunicorn` and `werkzeug` server packages.

Windows user will have to modify `werk.py` to point to where their virtualenv is.


### Development environment
Beginning with flask 0.11, run flask from the `cli` when doing development
```
  $ export FLASK_APP=my_application
  $ export FLASK_ENV=development
  $ flask run
```

For production simply do:
```
  $export FLASK_ENV=production
   modify config.py
```


## Running the app
`./guni` to run app on `gunicorn` server.
`./werk.py` to run app on `werkzeug` server.


## Checklist

- [ ] Responsive frontend design

## TODO

- [ ] Twiter integration

- [ ] Testing on various screens/devices.


## License
- Pending
