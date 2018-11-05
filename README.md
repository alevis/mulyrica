# Mulyrica
A tool for analyzing and providing useful insights into lyrics. 
```
Inputs: Song and Author
Outputs: Sentiment 
```
This web application runs on port `5000`

## Preliminaries
You might have to install the `vader_lexicon` package (Will fix this) to use the
`SentimentIntensityAnalyzer`.
Run this in `python shell` after activating venv` `nltk.download('vader_lexicon').`

## Activating virtualenvironment
- **Linux** users go to `webapp/venv/bin/` and run `source activate`.
Also edit `run.py` to ensure that the path to python is `venv/bin/python/`
- **Windows** users go to `mulyrica/Scripts/` and run `activate.`
Also edit `run.py` accordingly as shown above.

## Development environment
Beginning with flask 0.11, run flask from the `cli` when doing development
```
  $ export FLASK_APP=my_application
  $ export FLASK_ENV=development
  $ flask run
```
For production simply do:
 ```
if __name__=='__main__':
  app.run(host='127.0.0.1') # setting the host ip addr is optional
```
## Running
- `chmod a+x run.py`
- Then do `./run.py` and navigate to `http://localhost:5000`

# Running
- `chmod a+x run.py`
- Then do `./run.py` and navigate to `http://localhost:5000`


