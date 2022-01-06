def handler(event,context):
  return {
    'body': 'Hello there {0}'.format(event['requestContext']['identity']['sourceIp']),
    'headers': {
      'Content-Type': 'text/plain'
    },
    'statusCode': 200
  }
