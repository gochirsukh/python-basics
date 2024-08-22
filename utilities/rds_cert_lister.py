import boto3

# Create an RDS client
rds_client = boto3.client('rds')

def list_rds_instances_and_certs():
    # Describe all RDS instances
    response = rds_client.describe_db_instances()

    # Loop through the instances and print their certificate details
    for db_instance in response['DBInstances']:
        instance_id = db_instance['DBInstanceIdentifier']
        cert_id = db_instance['CertificateDetails']['CAIdentifier']        
        print(f"RDS Instance: {instance_id}, Certificate: {cert_id}")


if __name__ == "__main__":
    list_rds_instances_and_certs()