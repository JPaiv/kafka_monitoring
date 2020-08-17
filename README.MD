# Definition

Monitoring tool for web tracking with Apache kafka.

## Deployment

Deploy these AWS Lambda function with nameless-deploy-tools: https://github.com/NitorCreations/nameless-deploy-tools
This is the default deployment tool to automate quick deployment of these services.

### How to run

After deployment the lambda functions will make a request to the website and get data. This data is then parsed and then sent from producer to consumer. Consumer will then write the data to database and the content text is saved to s3 as a json.

At this point local run is possible but user must set environmental variables manually so it is not recommended to run anywhere except in AWS.
