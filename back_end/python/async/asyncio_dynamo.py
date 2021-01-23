# -*- coding: utf-8 -*-

import asyncio
import aioboto3


from boto3.dynamodb.conditions import Key


async def main():
    async with aioboto3.resource('dynamodb', region_name='ap-northeast-2') as dynamo_resource:
        table = await dynamo_resource.Table('test.ws-record')

        await table.put_item(
            Item={'key': 'test1', 'ref_dt': '20210123', 'option': 'some_data'}
        )

        result = await table.query(
            KeyConditionExpression=Key('key').eq('test1')
        )

        print(result['Items'])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
