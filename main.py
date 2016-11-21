# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Sample application that demonstrates how to use the App Engine Images API.

For more information, see README.md.
"""

# [START all]
# [START thumbnailer]
from google.appengine.api import images
from google.appengine.ext import ndb

import webapp2

class Thumbnailer(webapp2.RequestHandler):
    def get(self):

        if self.request.get("imgPath"):
            try:
                photoURL = images.get_serving_url(None, filename=self.request.get("imgPath"), secure_url=True)
            except images.ObjectNotFoundError as e:
                    self.response.set_status(404, e)
            if photoURL:
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write(photoURL)
                return
        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
        self.error(404)
# [END thumbnailer]


app = webapp2.WSGIApplication([('/img', Thumbnailer)], debug=True)
# [END all]
