from stashy.Stashy import Stashy

__author__ = 'Stashy.io'
__version__ = '0.0.1'

# The default Boto3 session; autoloaded when needed.
STASHY = None


def authorize(api_key):
    """
    Create a resource service client by name using the default session.
    """
    return _get_stashy().resource(api_key)


def setup_stashy(api_key):
    """
    Set up stashy, passing through any parameters to the session
    constructor. There is no need to call this unless you wish to pass custom
    parameters, because a default session will be created for you.
    """
    global STASHY
    STASHY = Stashy(api_key)


def _get_stashy(api_key):
    """
    Get the default session, creating one if needed.
    :rtype: :py:class:`~boto3.session.Session`
    :return: The default session
    """
    if STASHY is None:
        setup_stashy(api_key)

    return STASHY
