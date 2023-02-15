# City vistor recommendation service

This app helps finding places in cities to visit based on interest using the OpenAI's ChatGPT model.

## Installation

Run `bin/install.sh`

## Running the app

### API

Run `bin/run-dev.sh`

### Running the web app

Run `cd ui && yarn dev`

## Testing API

### Using `curl`

```bash
$ curl 'http://localhost:5000/api/v1/recommendation' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Origin: http://localhost:3000' \
  -H 'Referer: http://localhost:3000/' \
  --data-raw '{"city":"Monaco","interests":["Restaurants","bars","casino","Shopping"]}' \
  --compressed
```
