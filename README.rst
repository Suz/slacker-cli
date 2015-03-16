===========
slacker-cli
===========

.. image:: https://travis-ci.org/juanpabloaj/slacker-cli.svg?branch=master
    :target: https://travis-ci.org/juanpabloaj/slacker-cli
.. image:: https://coveralls.io/repos/juanpabloaj/slacker-cli/badge.png?branch=master
    :target: https://coveralls.io/r/juanpabloaj/slacker-cli?branch=master
.. image:: https://pypip.in/v/slacker-cli/badge.png
    :target: https://pypi.python.org/pypi/slacker-cli


Send messages to `Slack <https://slack.com/>`_ from command line.

Usage
=====

.. code-block:: bash

    date | slacker -c slack_channel -t slack_token

Slack Token can be called from a enviroment variable, called ``SLACK_TOKEN``.

You can set ``SLACK_TOKEN`` in your ``~/.bashrc``. Or you can use a shell script to call it with the -t option. 

.. code-block:: bash

    # ~/.bashrc
    export SLACK_TOKEN="slack_token_string"

.. code-block:: bash

    date | slacker -c slack_channel

Send message to user

.. code-block:: bash

    date | slacker -u user_name

Send message to #real_engineering and echo binary to a user or a channel (message is signed as 'bot')

.. code-block:: bash

    date | slacker -u user_name -b
    date | slacker -c slack_channel -b

Upload file to channel:

.. code-block:: bash

    date | slacker -c slack_channel -f image.png

Installation
============

.. code-block:: bash

    pip install slacker-cli

Contributors
============

- `JuanPablo AJ <https://github.com/juanpabloaj>`_
- `Marc Abramowitz <https://github.com/msabramo>`_
- `David Yen <https://github.com/davidyen1124>`_
- `Valentin Lab <https://github.com/vaab>`_
- `Suzanne Kiihne <https://github.com/suz>`_
