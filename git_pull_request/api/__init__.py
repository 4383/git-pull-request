# -*- encoding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from urllib.parse import urlparse


class API:
    @staticmethod
    def factory(origin):
        parsed_uri = urlparse(origin)
        domain = parsed_uri.netloc
        print(domain)
        binding = {
            "github.com": Github,
            "gitlab.com": Gitlab,
        }
        return binding.get(domain, OnPremise)()


class BaseHub:
    def connect(self, user, password, **kwargs):
        raise NotImplemented

    def get_repo(self, username, reponame):
        raise NotImplemented

    def get_pull(self, pull_number):
        raise NotImplemented


class Github(BaseHub):
    pass


class Gitlab(BaseHub):
    pass


class OnPremise:
    pass
