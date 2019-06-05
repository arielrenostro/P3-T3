#!/bin/sh

gunicorn rest.app:app -b 0.0.0.0:8080