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
import os
import unittest

import fixtures

import git_pull_request as gpr
from git_pull_request.api import API
from git_pull_request.api import Gitlab, Github, OnPremise

import github


class TestAPI(fixtures.TestWithFixtures):
    def setUp(self):
        self.tempdir = self.useFixture(fixtures.TempDir()).path
        os.chdir(self.tempdir)
        gpr._run_shell_command(["git", "init", "--quiet"])
        gpr._run_shell_command(["git", "remote", "add", "origin",
                                "https://github.com/jd/git-pull-request.git"])
        gpr._run_shell_command(["git", "config", "branch.master.merge",
                                "refs/heads/master"])
        gpr._run_shell_command(["git", "config", "branch.master.remote",
                                "origin"])

    def test_factory(self):
        api = API.factory("master")
        op = OnPremise()
        self.assertEqual(type(op),
                         type(api))

        gh = Github()
        api = API.factory("http://github.com/jd/git-pull-request.git")
        self.assertEqual(type(gh),
                         type(api))

        gt = Gitlab()
        api = API.factory("http://gitlab.com/jd/git-pull-request.git")
        self.assertEqual(type(gt),
                         type(api))
