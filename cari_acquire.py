"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List
import requests

from env import github_token

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Replace YOUR_GITHUB_USERNAME below with your github username.
# TODO: Add more repositories to the `repos` list.

repos = ['AIDungeon/AIDungeon',
             'rclone/rclone',
             'marblexu/PythonPlantsVsZombies',
             'redox-os/orbtk',
             'sailay1996/UAC_Bypass_In_The_Wild',
             'ruanyf/weekly',
             'alirezadir/Production-Level-Deep-Learning',
             'sdmg15/Best-websites-a-programmer-should-visit',
             'practicalAI/practicalAI',
             'HuaweiJoke/Huawei-Joke',
             'trekhleb/javascript-algorithms',
             '521xueweihan/HelloGitHub',
             'getify/You-Dont-Know-JS',
             'kdn251/interviews',
             'eavichay/microfronts',
             'goldbergyoni/nodebestpractices',
             'wuyouzhuguli/SpringAll',
             'halo-dev/halo',
             'serverless/serverless',
             'prometheus/client_golang',
             'VMadalin/kotlin-sample-app',
             'davidfowl/FeatherHttp',
             '0vercl0k/CVE-2019-11708',
             'mrdoob/three.js',
             'OfficeDev/office-ui-fabric-react',
             'standard/standard',
             'eslint/eslint',
             'jshint/jshint',
             'clutchski/coffeelint',
             'csscomb/csscomb.js',
             'sds/scss-lint',
             'htmlhint/HTMLHint',
             'validator/validator',
             'CSSLint/csslint',
             'PyCQA/pycodestyle',
             'PyCQA/flake8',
             'psf/black',
             'checkstyle/checkstyle',
             'rubocop-hq/rubocop',
             'oclint/oclint',
             'golang/lint',
             'ndmitchell/hlint',
             'coala/coala',
             'pre-commit/pre-commit',
             'innogames/igcommit',
             'fivethirtyeight/data',
             'datadesk/notebooks',
             'nytimes/objective-c-style-guide',
             'newsapps/beeswithmachineguns',
             'voxmedia/meme',
             'propublica/guides',
             'censusreporter/censusreporter',
             'nprapps/app-template',
             'TimeMagazineLabs/babynames',
             'guardian/frontend',
             'dukechronicle/chronline',
             'BloombergMedia/whatiscode',
             'times/cardkit',
             'mkiser/WTFJHT',
             'twbs/bootstrap',
             'daneden/animate.css',
             'nathansmith/960-Grid-System',
             'necolas/normalize.css',
             'ionic-team/ionicons',
             'designmodo/Flat-UI',
             'h5bp/html5-boilerplate',
             'foundation/foundation-sites',
             'Modernizr/Modernizr',
             'twbs/ratchet',
             'IanLunn/Hover',
             'connors/photon',
             'basscss/basscss',
             'atlemo/SubtlePatterns',
             'mrmrs/colors',
             'beetbox/beets',
             'scottschiller/SoundManager2',
             'CreateJS/SoundJS',
             'musescore/MuseScore',
             'tomahawk-player/tomahawk',
             'cashmusic/platform',
             'mopidy/mopidy',
             'AudioKit/AudioKit',
             'Soundnode/soundnode-app',
             'gillesdemey/Cumulus',
             'metabrainz/picard',
             'overtone/overtone',
             'samaaron/sonic-pi',
             'puppetlabs/puppet',
             'chef/chef',
             'ansible/ansible',
             'saltstack/salt',
             'hashicorp/vagrant',
             'openstack/openstack',
             'moby/moby',
             'capistrano/capistrano',
             'statsd/statsd',
             'graphite-project/graphite-web',
             'elastic/logstash',
             'fabric/fabric',
             'grafana/grafana',
             'StackStorm/st2',
             'openshift/origin',
             'getsentry/sentry',
             'deployphp/deployer',
             'kubernetes/kubernetes',
             'netdata/netdata',
             'cloud66-oss/habitus']

headers = {
    "Authorization": f"token {github_token}",
    "User-Agent": "cari-holmes",
}

if (
    headers["Authorization"] == "token"
    or headers["User-Agent"] == ""
):
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> requests.Response:
    return requests.get(url, headers=headers)


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    return github_api_request(url).json()["language"]


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    return github_api_request(url).json()


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists
    the files in a repo and returns the url that can be
    used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns
    a dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": requests.get(get_readme_download_url(contents)).text,
    }


def scrape_github_data():
    """
    Loop through all of the repos and process them. Saves the data in
    `data.json`.
    """
    data = [process_repo(repo) for repo in repos]
    json.dump(data, open("data.json", "w"))


if __name__ == "__main__":
    scrape_github_data()