# Batch Geocoding with Python and Google Geocoding API

This repository contains a python script to geocode multiple addresses using the Google Geocoding API.

Addresses can be geocoded for free at a rate of 2500 addresses per day, limited by Google. With a Google Developer API key, any number of addresses can be geocoded.

If the geocode does not succeed as address not found, script does google web search to get spelling suggestions. You  may need to enter your own API Key for Google Search. There is a limit of 100 per day for the free tier

Data input and output is processed from CSV files.
