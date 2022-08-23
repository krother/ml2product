
# ML2 Product

Course in productionizing a ML use case

## Pre-course questions

* have you trained a ML model before?
* have you used git before?
* have you written automated tests before?
* have you used Docker?
* is Docker installed on your computer?

## Contents

### Kick-Off

* expectations
* course overview

### Session 1: The Prototype

* train a simple ML model in a Jupyter notebook
* report a quality metric for the model
* recap questions: which model/metric/test strategy

### Session 2: Git

* Create a git repo and upload your code
* checklist for new repositories

### Session 3: Clean up

* export from Jupyter to a Python script
* remove unnecessary code
* structure code into functions
* run a linter
* git push

### Session 4: MLFlow

* create a MLFlow instance
* train a newer model with extra data
* compare the scores
* start a API via MLFlow

### Session 5: Test

* write a Unit Test against the API
* plug the test into GitHub action
* git push

### Session 6: Packaging

* write a file listing all dependencies
* use poetry to install/build/release the package
* git push

### Session 7: Monitor

* set up a cronjob that trains the model repeatedly
* log train scores over time
* plot the training scores
* discuss model drift

### Session 8: Data quality checks

* calculate metrics from key features from the training data
* use window functions to
* detect outliers
* add 3-4 plots to a dashboard

### Session 9: Dockerize

* write a Dockerfile
* run the docker container locally
* add a second docker container with a dashboard

### Session 10: Summary and Recap

* review

----

## Contact

`kristian.rother@posteo.de`

## License

(c) 2022 Dr. Kristian Rother

All code is subject to the MIT License. See License for details.

The course documentation is subject to the Creative Commons Attribution Share-Alike License 4.0 (CC-BY-SA 4.0).
See [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/) for details.
