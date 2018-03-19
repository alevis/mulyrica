# Mulyrica
This web application runs on port `5000`

## Preliminaries
You might have to install the `vader_lexicon` package (Will fix this) to use the
`SentimentIntensityAnalyzer`.
Run this in `python shell` after activating `lxenv` `nltk.download('vader_lexicon').`

## Activating virtualenvironment
- **Linux** users go to `webapp/lxenv/bin/` and run `source activate`.
Also edit `run.py` to ensure that the path to python is `lxenv/bin/python/`
- **Windows** users go to `mulyrica/Scripts/` and run `activate.`
Also edit `run.py` accordingly as shown above.

## Running
- `chmod a+x run.py`
- Then do `./run.py` and navigate to `http://localhost:5000`
