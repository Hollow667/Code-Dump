#!/usr/bin/env python
#
# cert-stream.py
# Stream the SSL certificates that Shodan is collecting at the moment
#
# WARNING: This script only works with people that have a subscription API plan!
# And by default the Streaming API only returns 1% of the data that Shodan gathers.
# If you wish to have more access please contact us at sales@shodan.io for pricing
# information.
#
# Author: achillean

import shodan
import sys

# Configuration
API_KEY = 'YOUR API KEY'

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)

    print 'Listening for certs...'
    for banner in api.stream.ports([443, 8443]):
                if 'ssl' in banner:
                        # Print out all the SSL information that Shodan has collected
                        print banner['ssl']

except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)
