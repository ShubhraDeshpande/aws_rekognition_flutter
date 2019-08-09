import json
import boto3
from decimal import Decimal
import urllib

print('Loading function')

rekognition = boto3.client('rekognition')

def detect_faces(bucket, key):
    response = rekognition.detect_faces(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    return response


def detect_labels(bucket,key):
    response = rekognition.detect_labels(Image={"S3Object":{"Bucket": bucket, "Name": key}})
    return response


# def lambda_handler(event, context):
    
#     bucket = event['Records'][0]['s3']['bucket']['name']
#     key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
#     try:
#         response = detect_faces(bucket, key)
#         print(response)
        
#         return response
#     except Exception as e:
#         print(e)
#         print("Error processing object {} from bucket {}. ".format(key, bucket) +
#               "Make sure your object and bucket exist and your bucket is in the same region as this function.")
#         raise e


def hello(event, context):
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        # Calls rekognition DetectFaces API to detect faces in S3 object
        response = detect_labels(bucket, key)
        print(response)
        
        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket) +
              "Make sure your object and bucket exist and your bucket is in the same region as this function.")
        raise e

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
