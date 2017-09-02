BrittleWit GAE Twitter Auth Demo
================================

This is a skeleton app for 
[Google App Engine's standard python environment](https://cloud.google.com/appengine/docs/standard/python/). 
It uses [flask with blueprints](http://flask.pocoo.org/docs/0.12/blueprints/). 

Assuming you have a working Google Cloud environment on your development machine, execute,
```sh
git clone https://github.com/jbn/brittle_wit_gae.git
cd brittle_wit_gae
make install_requirements 
```

Then, edit app.yml such that,

```yaml
# ...
env_variables:
  TWITTER_APP_KEY: [YOUR KEY]
  TWITTER_APP_SECRET: [YOUR SECRET]
# ...
```

Finally,

```sh
make devel
```
and visit [http://localhost:8080](http://localhost:8080)
