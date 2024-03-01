# Problem Definition
- Use case(s) and business goal
- Requirements
  - Scope (features needed), scale, and personalization
  - Performance: prediction latency, scale of prediction
  - Constraints
- Data: sources and availability
- Assumptions
- Translate an abstract problem into an ML problem 
  - ML objective,
  - ML I/O,
  - ML category (e.g. binary classification, multi-classification, unsupervised learning, etc)
# Success metric
- Engagement, impression, click rate.
- How to define metric in more detail.
- Should we optimize latency in inference vs accuracy?
- Offline vs online predictions?
- Classification:
  - Precision, Recall, F1.
  - Is precision or recall more important.
  - AUC (Area under the ROC curve): 
    - Run for different classification thresholds.
    - Y axis: True positive rate.
    - X axis: False positive rate.
- Regression:
  - MSE, MAE.
- Retrival and Ranking:
  - Precision@k, Recall@k
  - nDCG (Normalized discounted cumulative gain):
    - nDCG = DCG / IDCG
    - DCG: \sum gain/log(i+1) where i is the rank. 
      - Relevant items on top has more gain.
    - IDCG (Ideal discounted cumulative gain):
      - What is the ideal gain? 
        - Top5 relevant the rest is irrelavant.
        - All Top10 is relevant.
- Model performance is not same as business performance due to:
  - Business value saturation (no more room to improve)
  - Over-optimization on a metric.
    - More clicks may not lead to more conversion.
- Online metrics:
  - CTR
  - Task success/failure rate.
  - Conversion rate.

# Data
- What kind of data do we have?
  - Stream.
  - PII (Personal Identifying Information)
- Do we need data pre-processing?
  - Feature engineering.
  - In-balanced data.
  - Manual labelling.
- Train-test split:
  - k-fold cross validation.
  - Stratified train-test split
    - Only for classification.
    - Makes sure each class has same distributes between sets.
    - Optionally we can cluster first and use these labels.

# Define features
- Explain most important features in more detail.
- How will the data look like?

# Define model
- Explain model in more detail.
- Compare to baseline.
- Do we need to explain predictions?
- Debugging the model:
  - Start with the small version of model (NN) or less parameters.
  - Overfit a small amount of data.
  - Increase gradually.
- Training model across multiple devices
  - Model Parallelism: split model into multiple devices.
    - Horizontal: Each layer in different machines.
      - Not efficient for fully connected layers.
      - Each layer waits for the output of the previous layer.
    - Vertical: e.g. left half, and right half in different machines.
      - No efficient for fully connected layers.
      - Next layer wait for the output of both halves.
  - Data Parallelism: Split data into multiple devices.
    - Gradients are averaged.
    - Mirrored Strategy:
      - All model parameters are always same between replicas.
      - AllReduce algorithm collects gradients, averages them and distributes.
      - Synchronous.
      - Faster on a single machine.
    - Centralized parameters:
      - One server keeps the parameters.
      - Can run either synchronous or asynchronous.
      - Synchronous:
        - Replicas calculate gradients, send to server and wait for the update.
        - Ignore slowest N replicates to speed up.
        - Bandwith problems
          - The server sends gradients to all replicas at the same time.
        - Asynchronous:
          - Replicas don't wait server and continue the next batch.
          - Stale gradients problem.
          - Reduce learning rate.
          - Adjust mini-batch size.
          - Start with a single replica and scale others later.
          - Drop stale gradients.
    - Quantization:
      - Use INT8 instead of FLOAT32 for weights and activations.
      - Try when model inference is slow or the model is large. 
        
# Serving
- Do we need to train online?


# Monitoring
- Do we get feedback from users? How to use them.
- Segmentation
  - Location, age, gender, new vs old user.
- Data drift. How often do we train it?


# Tips
- Trade-offs.

# More Topics
## A/B Testing.
- Type I error: 
  - We reject the null hypothesis when we should not. 
  - We launch a change that makes no difference.
- Type II error:
  - We fail to reject null hypothesis when we should.
  - We decided not to launch a change we there was a difference.
- Significance:
  - Alpha. Probability to commit a Type I error. ~0.05
- Beta:
- (1-Power). Probability to commit a Type II error. ~0.05
- To calculate sample size, we also need to know:
  - Z-scores for alpha and beta.
  - mean and std of two distributions.

- https://medium.com/grabngoinfo/top-20-ab-test-interview-questions-and-answers-2d59cfc8c6df

- https://towardsdatascience.com/required-sample-size-for-a-b-testing-6f6608dd330a 
- https://www.stat.ubc.ca/~rollin/stats/ssize/n2.html
- https://towardsdatascience.com/understanding-power-analysis-in-ab-testing-14808e8a1554
- How long to run the tests. statistically significance.
- Success or fail. 

## Dataset size calculation.

user_id, item_id, score
 4 + 4 +4 = 12 bytes
number_of rows: 50 * 10^9
50 * 12gb = 600gb

- int doesn't have a limit in Python.
- int16 2 bytes (max: 30K)
- int32 4 bytes (max: 2 billion)
- float32 4 bytes.

- thousand	    10^3    1,000	              k (K)	kilo
- million	    10^6    1,000,000	          M	mega
- billion       10^9	1,000,000,000	      G	giga
- trillion      10^12	1,000,000,000,000     tera 
- quadrillion   10^15   1,000,000,000,000,000 peta  


# Common Trade-offs
- Latency vs Throughput
- Accuracy vs Latency
