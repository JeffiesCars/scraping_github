import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd
import acquire

def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    string = string.strip()
    string = string.replace('\n', ' ')
    return string 

def normalize(string):
    """
    Convert to all lowercase  
    Normalize the unicode chars  
    Remove any non-alpha or whitespace characters  
    Remove any alpha strings with 2 characters or less  
    """
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # keep only alpha chars
    string = re.sub(r'[^a-z]', ' ', string)
    # remove strings less than 2 chars in length
    string = re.sub(r'\b[a-z]{,2}\b', '', string)
    # convert newlines and tabs to a single space
    string = re.sub(r'[\r|\n|\r\n]+', ' ', string)
    # strip extra whitespace
    string = string.strip()
    return string    

def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string, return_str=True)

def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    text_stemmed = ' '.join(stems)
    return text_stemmed

def lemmatize(text):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text_lemmatized = ' '.join(lemmas)
    return text_lemmatized

def remove_stopwords(tokenized_string, extra_words=['https', 'http', 'github', 'www', 'email','gmail', 'com', 'AIDungeon',
 'AIDungeon',
 'rclone',
 'rclone',
 'marblexu',
 'PythonPlantsVsZombies',
 'redox-os',
 'orbtk',
 'sailay1996',
 'UAC_Bypass_In_The_Wild',
 'ruanyf',
 'weekly',
 'alirezadir',
 'Production-Level-Deep-Learning',
 'sdmg15',
 'Best-websites-a-programmer-should-visit',
 'practicalAI',
 'practicalAI',
 'HuaweiJoke',
 'Huawei-Joke',
 'trekhleb',
 'javascript-algorithms',
 '521xueweihan',
 'HelloGitHub',
 'getify',
 'You-Dont-Know-JS',
 'kdn251',
 'interviews',
 'eavichay',
 'microfronts',
 'goldbergyoni',
 'nodebestpractices',
 'wuyouzhuguli',
 'SpringAll',
 'halo-dev',
 'halo',
 'serverless',
 'serverless',
 'prometheus',
 'client_golang',
 'VMadalin',
 'kotlin-sample-app',
 'davidfowl',
 'FeatherHttp',
 '0vercl0k',
 'CVE-2019-11708',
 'mrdoob',
 'three.js',
 'OfficeDev',
 'office-ui-fabric-react',
 'standard',
 'standard',
 'eslint',
 'eslint',
 'jshint',
 'jshint',
 'clutchski',
 'coffeelint',
 'csscomb',
 'csscomb.js',
 'sds',
 'scss-lint',
 'htmlhint',
 'HTMLHint',
 'validator',
 'validator',
 'CSSLint',
 'csslint',
 'PyCQA',
 'pycodestyle',
 'PyCQA',
 'flake8',
 'psf',
 'black',
 'checkstyle',
 'checkstyle',
 'rubocop-hq',
 'rubocop',
 'oclint',
 'oclint',
 'golang',
 'lint',
 'ndmitchell',
 'hlint',
 'coala',
 'coala',
 'pre-commit',
 'pre-commit',
 'innogames',
 'igcommit',
 'fivethirtyeight',
 'data',
 'datadesk',
 'notebooks',
 'nytimes',
 'objective-c-style-guide',
 'newsapps',
 'beeswithmachineguns',
 'voxmedia',
 'meme',
 'propublica',
 'guides',
 'censusreporter',
 'censusreporter',
 'nprapps',
 'app-template',
 'TimeMagazineLabs',
 'babynames',
 'guardian',
 'frontend',
 'dukechronicle',
 'chronline',
 'BloombergMedia',
 'whatiscode',
 'times',
 'cardkit',
 'mkiser',
 'WTFJHT',
 'twbs',
 'bootstrap',
 'daneden',
 'animate.css',
 'nathansmith',
 '960-Grid-System',
 'necolas',
 'normalize.css',
 'ionic-team',
 'ionicons',
 'designmodo',
 'Flat-UI',
 'h5bp',
 'html5-boilerplate',
 'foundation',
 'foundation-sites',
 'Modernizr',
 'Modernizr',
 'twbs',
 'ratchet',
 'IanLunn',
 'Hover',
 'connors',
 'photon',
 'basscss',
 'basscss',
 'atlemo',
 'SubtlePatterns',
 'mrmrs',
 'colors',
 'beetbox',
 'beets',
 'scottschiller',
 'SoundManager2',
 'CreateJS',
 'SoundJS',
 'musescore',
 'MuseScore',
 'tomahawk-player',
 'tomahawk',
 'cashmusic',
 'platform',
 'mopidy',
 'mopidy',
 'AudioKit',
 'AudioKit',
 'Soundnode',
 'soundnode-app',
 'gillesdemey',
 'Cumulus',
 'metabrainz',
 'picard',
 'overtone',
 'overtone',
 'samaaron',
 'sonic-pi',
 'puppetlabs',
 'puppet',
 'chef',
 'chef',
 'ansible',
 'ansible',
 'saltstack',
 'salt',
 'hashicorp',
 'vagrant',
 'openstack',
 'openstack',
 'moby',
 'moby',
 'capistrano',
 'capistrano',
 'statsd',
 'statsd',
 'graphite-project',
 'graphite-web',
 'elastic',
 'logstash',
 'fabric',
 'fabric',
 'grafana',
 'grafana',
 'StackStorm',
 'st2',
 'openshift',
 'origin',
 'getsentry',
 'sentry',
 'deployphp',
 'deployer',
 'kubernetes',
 'kubernetes',
 'netdata',
 'netdata',
 'cloud66-oss',
 'habitus'], exclude_words=[]):
    words = tokenized_string.split()
    stopword_list = stopwords.words('english')
    # remove the excluded words from the stopword list
    stopword_list = set(stopword_list) - set(exclude_words)
    # add in the user specified extra words
    stopword_list = stopword_list.union(set(extra_words))
    filtered_words = [w for w in words if w not in stopword_list]
    final_string = " ".join(filtered_words)
    return final_string 

def prep_contents(df):
    df = df.assign(original = df.readme_contents)
    df = df.assign(normalized = df.original.apply(normalize))
    df = df.assign(stemmed = df.normalized.apply(stem))
    df = df.assign(lemmatized = df.normalized.apply(lemmatize))
    df = df.assign(cleaned = df.lemmatized.apply(remove_stopwords))
    return df

def clean(string):
    "a simple function to prepare text data"
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words("english") + ["r", "u", "2", "ltgt"]
    string = (
        unicodedata.normalize("NFKD", string)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
        .lower()
    )
    words = re.sub(r"[^\w\s]", "", string).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]