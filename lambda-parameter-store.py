# Execution Profile
"""
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ssm:GetParameter",
            "Resource": "arn:aws:ssm:REGION:ACCOUNT_ID:parameter/NOME_DO_PARAMETRO"
        }
    ]
}
"""
#
#
#

import boto3
import os

def lambda_handler(event, context):
    ssm = boto3.client('ssm')

    parameter_name = "/meu/parametro"

    try:
        response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)        
        parametro_valor = response['Parameter']['Value']
        
        return {
            'statusCode': 200,
            'body': f"Valor do parâmetro: {parametro_valor}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Erro ao obter parâmetro: {str(e)}"
        }


