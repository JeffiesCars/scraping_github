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

repos = ['https://github.com/AIDungeon/AIDungeon',
 'https://github.com/rclone/rclone',
 'https://github.com/marblexu/PythonPlantsVsZombies',
 'https://github.com/redox-os/orbtk',
 'https://github.com/sailay1996/UAC_Bypass_In_The_Wild',
 'https://github.com/ruanyf/weekly',
 'https://github.com/alirezadir/Production-Level-Deep-Learning',
 'https://github.com/sdmg15/Best-websites-a-programmer-should-visit',
 'https://github.com/practicalAI/practicalAI',
 'https://github.com/HuaweiJoke/Huawei-Joke',
 'https://github.com/trekhleb/javascript-algorithms',
 'https://github.com/521xueweihan/HelloGitHub',
 'https://github.com/getify/You-Dont-Know-JS',
 'https://github.com/kdn251/interviews',
 'https://github.com/eavichay/microfronts',
 'https://github.com/goldbergyoni/nodebestpractices',
 'https://github.com/wuyouzhuguli/SpringAll',
 'https://github.com/halo-dev/halo',
 'https://github.com/serverless/serverless',
 'https://github.com/prometheus/client_golang',
 'https://github.com/VMadalin/kotlin-sample-app',
 'https://github.com/davidfowl/FeatherHttp',
 'https://github.com/0vercl0k/CVE-2019-11708',
 'https://github.com/mrdoob/three.js',
 'https://github.com/OfficeDev/office-ui-fabric-react',
 'https://github.com/standard/standard',
 'https://github.com/eslint/eslint',
 'https://github.com/jshint/jshint',
 'https://github.com/clutchski/coffeelint',
 'https://github.com/csscomb/csscomb.js',
 'https://github.com/sds/scss-lint',
 'https://github.com/htmlhint/HTMLHint',
 'https://github.com/validator/validator',
 'https://github.com/CSSLint/csslint',
 'https://github.com/PyCQA/pycodestyle',
 'https://github.com/PyCQA/flake8',
 'https://github.com/psf/black',
 'https://github.com/checkstyle/checkstyle',
 'https://github.com/rubocop-hq/rubocop',
 'https://github.com/oclint/oclint',
 'https://github.com/golang/lint',
 'https://github.com/ndmitchell/hlint',
 'https://github.com/coala/coala',
 'https://github.com/pre-commit/pre-commit',
 'https://github.com/innogames/igcommit',
 'https://github.com/fivethirtyeight/data',
 'https://github.com/datadesk/notebooks',
 'https://github.com/nytimes/objective-c-style-guide',
 'https://github.com/newsapps/beeswithmachineguns',
 'https://github.com/voxmedia/meme',
 'https://github.com/propublica/guides',
 'https://github.com/censusreporter/censusreporter',
 'https://github.com/nprapps/app-template',
 'https://github.com/TimeMagazineLabs/babynames',
 'https://github.com/guardian/frontend',
 'https://github.com/dukechronicle/chronline',
 'https://github.com/BloombergMedia/whatiscode',
 'https://github.com/times/cardkit',
 'https://github.com/mkiser/WTFJHT',
 'https://github.com/twbs/bootstrap',
 'https://github.com/daneden/animate.css',
 'https://github.com/nathansmith/960-Grid-System',
 'https://github.com/necolas/normalize.css',
 'https://github.com/ionic-team/ionicons',
 'https://github.com/designmodo/Flat-UI',
 'https://github.com/h5bp/html5-boilerplate',
 'https://github.com/foundation/foundation-sites',
 'https://github.com/Modernizr/Modernizr',
 'https://github.com/twbs/ratchet',
 'https://github.com/IanLunn/Hover',
 'https://github.com/connors/photon',
 'https://github.com/basscss/basscss',
 'https://github.com/atlemo/SubtlePatterns',
 'https://github.com/mrmrs/colors',
 'https://github.com/beetbox/beets',
 'https://github.com/scottschiller/SoundManager2',
 'https://github.com/CreateJS/SoundJS',
 'https://github.com/musescore/MuseScore',
 'https://github.com/tomahawk-player/tomahawk',
 'https://github.com/cashmusic/platform',
 'https://github.com/mopidy/mopidy',
 'https://github.com/AudioKit/AudioKit',
 'https://github.com/Soundnode/soundnode-app',
 'https://github.com/gillesdemey/Cumulus',
 'https://github.com/metabrainz/picard',
 'https://github.com/overtone/overtone',
 'https://github.com/samaaron/sonic-pi',
 'https://github.com/puppetlabs/puppet',
 'https://github.com/chef/chef',
 'https://github.com/ansible/ansible',
 'https://github.com/saltstack/salt',
 'https://github.com/hashicorp/vagrant',
 'https://github.com/openstack/openstack',
 'https://github.com/moby/moby',
 'https://github.com/capistrano/capistrano',
 'https://github.com/statsd/statsd',
 'https://github.com/graphite-project/graphite-web',
 'https://github.com/elastic/logstash',
 'https://github.com/fabric/fabric',
 'https://github.com/grafana/grafana',
 'https://github.com/StackStorm/st2',
 'https://github.com/openshift/origin',
 'https://github.com/getsentry/sentry',
 'https://github.com/deployphp/deployer',
 'https://github.com/kubernetes/kubernetes',
 'https://github.com/netdata/netdata',
 'https://github.com/cloud66-oss/habitus']

headers = {
    "Authorization": f"token {github_token}",
    "User-Agent": "JeffiesCars",
}

if (
    headers["Authorization"] == f'{github_token}'
    or headers["User-Agent"] == "Jeff-Hutchins"
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