# Given
Create a recommender system for advertiser sellers in an e-commerce website.
Seller create campaigns to promote their items.
They can choose keywords to be used for promotion.
# Define the problem
- We want to create a model that can help sellers:
  - to find keywords for their campaigns.
  - a good keyword should increase the sales through the campaign.
- Keywords are free format. low quality.
  - May need a clustering phase in advance.
- Raw data:
  - Historical Campaign Data:
    - product metadata
    - keywords
    - campaign category
    - ad rate
    - impressions
    - conversion
    - purchase
    - 
  - Product:
    - title
    - category
    - price
    - number of items in the category
    - number of clicks/purchases in last n days.
    - shipping
    - item spec
    - condition
  - Search data
    - keyword.
    - clicked/purchased items.
  
- We can first find the most relevant keywords to the campaign item
- Then we can rank the keywords by probability to get clicks/purchases.

# Design the data processing pipeline
# Create a model architecture

## Product to relevant keywords model
- For a given product, return the most relevant keywords.
- Basic model:
  - Create embeddings for each keyword and product.
  - Add keywords to a vector search engine.
  - Query with the product embeddings.
  - Use a known embeddings model.
- Advance model:
  - We need to map keywords and the products into the same space.
  - Two tower model:
    - Tower one: keyword.
    - Tower two: product metadata
    - Output: clicked/purchased.
    - Needs negative sampling.
    - In run time:
      - We create embeddings for each keyword.
      - We push keywords to vector search engine.
      - We query with the product embeddings.

## Campaign item to keyword ranker.
- For a given campaign, product and keyword, return the purchase/click probability.
- We may choose to use the embeddings for the products and keywords.
- Otherwise, we can use their metadata and encodings.
- Ranker can be either linear regression, xgboost or neural network.
- Liner regression:
  - Easier to interpret with co-efficients.
  - Baseline. 
- Xgboost:
  - Non-linear. combination of weak learners.
  - Use SHAP values to interpret.
  - May overfit easily. tree depth, number of trees.
  - more robust to normalization.
  - uses labels out of the box.
- Neural network:
  - Non-linear. Can learn complex relations.
  - Less feature engineering.
  - Sensitive to quality of the data:
    - Null values.
    - outliers.
  - Need to measure the latency. quantization.

# Train the model
- Fine tune parameters
- monitor loss, accuracy on training and validation.
- Spark supports data parallelizm for Xgboost
- Pytorch supports data parallelizm for neural networks.
# Evaluate the model
- Each model has its own evaluation.
- We can evaluate the overall system as a ranking problem.
- For the successful campaigns in the test set:
  - Check if we can find the keywords in the recommendation list.
- If there are multiple keywords in the campaigns we can use:
  - normalized discounted cumulative gain.
- If single keyword, we can use mean reciprocal rank.
# Deploy and monitor the model
- We want measure if:
  - Sellers pick the recommended keywords.
  - Do the success of the campaigns increase if they pick a recommended keyword.
    - Success is based on the purchases/clicks.
- groupA: campaigns where no keywords recommended.
- groupB: campaigns where keywords recommended and used.
- Primary metric: purchase rate. 
  - at least one.
  - we may also use number of purchases.
- North Star: revenue.
- Guardrail: number of campaigns created.
- Secondary: 
  - clicks through search.
  - recommended keyword selection.

- null hypotheses: Using recommended keywords does not increase purchases.
- Power analysis:
  - effect size: 1% increase in purchases.
  - power: 80%
  - significance level: 0.05
- Analyse the primary and the other metrics.
- Make go, no go decision.
# Wrap up 