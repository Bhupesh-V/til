# Simulating AWS Lambda locally using LocalStack

## Pre-requisties

1. Install Docker & Start the demon (if not already running).
2. Install LocalStack according to your system requirements.
   1. Start the localstack process
   ```
   localstack start -d
   ```
3. Install [awslocal](https://github.com/localstack/awscli-local) latest version.


## Prepare your Lambda Function (Go Example)

### Create a simple Go Lambda Handler

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

type RequestBody struct {
	Num1 int `json:"num1"`
	Num2 int `json:"num2"`
}

func handler(ctx context.Context, request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	var body RequestBody
	err := json.Unmarshal([]byte(request.Body), &body)
	if err != nil {
		return events.APIGatewayProxyResponse{StatusCode: 400, Body: "Invalid request body"}, nil
	}

	product := body.Num1 * body.Num2
	responseBody := fmt.Sprintf("The product of %d and %d is %d", body.Num1, body.Num2, product)

	return events.APIGatewayProxyResponse{
		StatusCode: 200,
		Body:       responseBody,
	}, nil
}

func main() {
	lambda.Start(handler)
}
```

### Initialize Go project and tidy dependencies.

```
go mod init localstack-go-lambda-example
go mod tidy
```

### Build for Linux amd64.

```
GOOS=linux GOARCH=amd64 go build -o main main.go
```

Zip the binary (make sure to name the binary main).

```
zip main.zip main
```


## Create AWS Lambda

Go 1.x runtime is now unsupported on AWS. Refer documentation when setting up in real environment.

```sh
awslocal lambda create-function \
    --function-name localstack-go-lambda-example \
    --runtime go1.x \
    --zip-file fileb://main.zip \
    --handler main \
    --role arn:aws:iam::000000000000:role/lambda-role
```

Output Example

```json
{
    "FunctionName": "localstack-go-lambda-example",
    "FunctionArn": "arn:aws:lambda:us-west-1:000000000000:function:localstack-go-lambda-example",
    "Runtime": "go1.x",
    "Role": "arn:aws:iam::000000000000:role/lambda-role",
    "Handler": "main",
    "CodeSize": 5408451,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2024-07-23T19:26:58.271251+0000",
    "CodeSha256": "dY9rW1dQKjY0sS6/ijsx8B1ZtT8iQlO9qhTfCSieX9I=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "c5969abb-b2bf-4a41-967a-6d043b2f41bd",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Zip",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    }
}
```

## Invoke Lambda

Wait for a 5-10 seconds before invoking the lambda.

> Lambda execution on localstack is synchronus so you will not see live output

```sh
awslocal lambda invoke --function-name localstack-go-lambda-example \
    --cli-binary-format raw-in-base64-out \
    --payload '{"body": "{\"num1\": 10, \"num2\": 10}"}' output.txt
```

Or use the following command, when sending payload from a file (make sure the file contents are bas64 encoded).

```sh
awslocal lambda invoke \
    --function-name localstack-go-lambda-example \
    --payload file://encoded_payload \
    response.json
```

You should see lambda output in output.txt

```json
{
    "statusCode": 200,
    "headers": null,
    "multiValueHeaders": null,
    "body": "The product of 10 and 10 is 100"
}
```

## Resources

1. https://docs.localstack.cloud/user-guide/aws/lambda/#introduction
2. https://stackoverflow.com/questions/58133166/error-fork-exec-var-task-main-no-such-file-or-directory-while-executing-aws 