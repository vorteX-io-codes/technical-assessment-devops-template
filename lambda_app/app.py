"""Entry points for the application."""

import logging
import sys
from typing import Dict, NoReturn, Union

import click

logger = logging.getLogger()
logger.setLevel('INFO')


def process(message: str) -> str:
    """Process message. The application logic is impleted here.
    Nothing to change for the assessment

    Parameters
    ----------
    message : str
        input message

    Returns
    -------
    str
        processed message

    """
    return f"The received message is: '{message}'"


JSON = Dict[str, Union[int, str, float, 'JSON']]

LambdaEvent = JSON
LambdaContext = object
LambdaOutput = JSON


def lambda_handler(event: LambdaEvent, context: LambdaContext) -> LambdaOutput:  # noqa: ARG001
    """Entry point for Lambda function.

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    -------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html

    """

    # TODO: write the lambda handler in a *robust* maner to:
    # - fetch the message in the event body of the LambdaEvent
    # - call the above 'process' function with the message and get the returned value
    # - return the LambdaOutput with the following format:
    # {
    #        'statusCode': XXX,
    #        'body': 'Return_value_of_process_function',
    #    }
    #

    ...


@click.command()
@click.option('-m', '--message', required=True, help='Message')
def main(message: str) -> NoReturn:  # pragma: no cover
    """Entrypoint for application CLI.

    Parameters
    ----------
    message : str
        input message

    """
    consoleHandler = logging.StreamHandler(sys.stdout)
    logger.addHandler(consoleHandler)

    result = process(message)
    logger.info(result)

    sys.exit(0)


if __name__ == '__main__':  # pragma: no cover
    main()
