# CarroPerro: Car discovery driven by dogs (toy application)

The CarroPerro application recommends cars based on a user's affinity for
various kinds of dogs. The data it was trained on was generated by mining
Twitter for users who tweeted both dog-related hashtags and car-related
hastags. A latent factor model was learned with ALS, and that model is
used to predict which cars a user might like based on the knowledge of
which dogs they like. Evaluation shows performance well above a baseline
model which simply recommends the most popular cars to everyone.

This particular example of cross-domain learning is very limited,
and the model is hampered by the small amount of data I was able to collect,
but perhaps with several orders of magnitude more data, useful results could
be achieved.

# Setup

This project requires Python 3.6+. Before running any of the steps below,
you should clone this repository, activate the Python virtual environement,
and install the requirements.

```sh
git clone git@github.com:mrjf/carroperro.git
cd carroperro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# The data

The package ships with a list of car makes and models and dog breeds.
We use these strings to generate a set of hashtags.
We use the Twitter API to find users who have tweeted using one of these
hashtags, and then get their entire user timeline (up to the limit of
the Twitter API, about 3200 tweets), to see if they have used any of the
other hashtags in our set. We record all such hastags used in the user's
timeline, and then from this corpus of user data generate a coocurrence
table, so that we can see the number of times each hashtag has occurred
in the same user timeline as each other hashtag.

Because we are interested in predicting cars from dogs, we process the
data to remove car-car and dog-dog coocurrences and generate a matrix
with cars in the rows and dogs in the columns, and their coocurrence
counts in the cells. The full coocurrence data could also be useful in
other applications.

## Fetching the data

A sample data collection script is provided and can be run as follows:

`python -m scripts.fetch`

The main parameter to tune in the data collection process is the `user_limit`.
Defaulting to 25, this specifies the number of user timelines to fetch for
each hashtag. This is the main factor that influences the amount of time the
data collection takes. At 25, this can take 48 hours or more. 25 is still
a very sparse amount of data and does not lead to a robust solution. To
scale this process, I would estimate that at least 1000 users per hashtag
should be used. This data collection would need to be run in parallel
in multiple instances, using Twitter's premium or GNIP API services with
higher limits, in order to finish in a reasonable time period.

The coocurrences for individual hashtags are written out in JSON in one file
per hashtag, by defualt in `data/hashtag_coocs` in the top-level directory
of the repository. In order to be used for ALS, this data must be processed
to generate the table of coocurrence counts, and these are written by default
to `data/hashtag_counts.csv` after fetching completes. Edit these paths in
`scripts/fetch.py` if you wish.

## Data alternatives

Any source that lets us see users talking about both dogs and cars is a potential
data source for this recommender. Facebook or Reddit would be possible alternatives
for textual data, while Instagram or Flickr could be used for image data, which could
be analyzed on the basis of associated metadata, or using image analysis to recognize
car models and dog breeds.

# The API server

After data collection completes, the API server may be run. Running the API server
builds the ALS model based on the `data/hashtag_counts.csv` data. This completes
very quickly on this small data sample, but in a real-world scenario one would want
to build the model in advance and save it.

## Running the server

`python -m scripts.run`

By default the server runs on port `5002`.

The API exposes two endpoints:

### addData
`GET addData/<user_id>/<dog_id>` - adds information to the in-memory user store,
indicating an affinity on the part of the user assigned to __user_id__ for the dog with __dog_id__.
Calling the endpoint again with the same __user_id__ and __dog_id__ will increment the count for
that pair, although the affinity is treated as binary in this implementation and the
strength of association is not used. Any integer __user_id__ will be accepted by the system.
If the supplied __dog_id__ is not present in the system a 400 response is returned.

In a production system, this endpoint should be a `POST` operation, but here it is a
`GET` for ease of interaction in the browser. For example, visiting
`http://127.0.0.1:5002/addData/4/55` will add __dog_id__ 55, the Welsh Corgi, to __user_id__
4's affinity table.

### predictInterests
`GET predictInterests/<user_id>/` - returns a JSON array of the top 5 recommended
cars for the user with the supplied id, along with their scores. If the supplied
`__user_id__` is not present in the system a 400 response is returned. For convenience,
you may set the query param `names=true` to have the car names returned instead of their
ids. Note that because the ALS model building is not deterministic, and this data is
small and sparse, results are not stable across model instantiations, so restarting
the web service and re-renetering the same user data can result in different
recommendations.

Visiting `http://127.0.0.1:5002/predictInterests/4?names=true` will display the
predicted cars for __user_id__ 4.

# Evaluating the results

`python -m scripts.eval`

Running the evaluation script builds the ALS model in the same manner as running the
server does. Then we calculate the top 5 recommended cars for each dog and compare them
with the baseline recommender which always recommends the 5 most popular cars in America.
The metric on which we compare them is normalized discounted cumulative gain (NDCG),
a metric for evaluating ranked retrieval relevance which rewards the model for having
the most relevant documents near the top of the list. In this case, we take the ground
truth for relevance to be the count of coocurrences of the dog and car in question.

For each dog, the ALS model and the baseline model each suggest their top 5 cars, and
the suggested cars are replaced in a list with the count of their coocurrence with the
dog in the gathered data (or 0 if not observed). Those separate lists of counts for the
baseline and ALS models are then fed into the NDCG formula and the results compared.
Whichever model has the highest NDCG score for that dog is considered to have
returned the more relevant results.

On the supplied coocurrence dataset, the ALS model dramatically outperforms the baseline
model, usually achieving a higher NDCG on 50 or more of the 57 dogs. To make sure that
this result is statistically significant, we run a t-test over the two sets of NDCG
scores and obtain a p-value that is very small indeed, indicating that there is less
than a one in an octillion chance of these results occurring by chance.

Of course, the fact that the ALS recommender outperforms the baseline on this metric
does not guarantee that the ALS model is providing useful results. To believe that, you
should also believe that the ground truth (observed coocurrences) is a valid measure
and NDCG is an appropriate metric. In a real-world system, some form of A/B testing
would be an ideal way to evaluate the model, for example by showing some users
predictions from the baseline, and some predictions from ALS, and recording how many
users go on to buy one of the suggested vehicles.


# Running tests

Unit tests test the correctness of the Python code, not the recommender system itself.
They may be run as follows:

`python -m unittest discover -p "*_test.py"`
