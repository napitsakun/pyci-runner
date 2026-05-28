## Installation

### Clone the repository:
```
git clone https://github.com/napitsakun/pyci-runner.git
cd pyci-runner
```

### Create a virtual environment:
```
python -m venv venv
source venv/bin/activate
```

### Install dependencies:
```
pip install -r requirements.txt
```

### Configuration

Rename `.env.sample` to `.env` and set necessary environment variables.

### Usage

Run locally:
```
python script.py
```

Run through CI:
```
github actions -> workflow dispatch -> runner execution
```
