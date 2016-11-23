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
# [START getServingURL]
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.api import blobstore
import webapp2
from webapp2_extras import json

class GetServingURL(webapp2.RequestHandler):
    def get(self):

        if self.request.get("imgPath"):
            try:
                blobKey = blobstore.create_gs_key(self.request.get('imgPath'))
                photoURL = images.get_serving_url(blobKey, secure_url=True)
            except images.ObjectNotFoundError as e:
                    self.response.set_status(404, e)
            if photoURL:
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write(json.encode(photoURL))
                self.response.set_status(200)
                return
        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
        self.error(404)
    def delete(self):
        if self.request.get('imgPath'):
            try:
                blobKey = blobstore.create_gs_key(self.request.get('imgPath'))
                print(blobKey)
                images.delete_serving_url(blobKey)
            except images.Error as e:
                self.response.set_status(404, e)
            except image.InvalidBlobKeyError as e:
                self.response.set_status(404, e)
            except blobstore.Error as e:
                self.response.set_status(404, e)
# [END getServingURL]

# [START deleteServingURL]

# [END deleteServingURL]


app = webapp2.WSGIApplication([('/img', GetServingURL)], debug=True)
# [END all]
