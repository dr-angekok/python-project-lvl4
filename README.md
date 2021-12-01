### Hexlet tests and linter status:
[![Actions Status](https://github.com/dr-angekok/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/dr-angekok/python-project-lvl4/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/5282ffae128816be4306/maintainability)](https://codeclimate.com/github/dr-angekok/python-project-lvl4/maintainability)
[![Actions Status](https://github.com/dr-angekok/python-project-lvl3/workflows/Package%20tests/badge.svg)](https://github.com/dr-angekok/python-project-lvl4/actions)

This app is a simple task manager built as a Hexlet's course final project.

You can watch it at online work here:
https://angekoks-task-manager.herokuapp.com

For use localy:
``` 
git clone https://github.com/dr-angekok/python-project-lvl4
cd python-project-lvl4
```
you must have poetry installed to continue
```
make install
```
Now you should rename file env.example to .env and added value of variable environments

After this:
```
make migration
``` 
For start application:
```
make test-run
```
The application is locally available at [http://127.0.0.1:8000]

You should get something like that:

[![asciicast](https://asciinema.org/a/qrUmPioW8UcbRbkiA3PE8jZvO.svg)](https://asciinema.org/a/qrUmPioW8UcbRbkiA3PE8jZvO)