import subprocess, json, sys
from .state import State

class ANSI:
    RESET = '\033[0m'
    YELLOW = '\033[93m'

def fastfetch():
    try:
        result = subprocess.run(
            ['fastfetch', '--format', 'json'],
            capture_output=True, text=True, check=True
        )
        return {
            mod['type']: mod['result']
            for mod in json.loads(result.stdout)
            if 'result' in mod
        }
    except FileNotFoundError:
        print(f"{ANSI.YELLOW}error: fastfetch command not found.{ANSI.RESET}", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"{ANSI.YELLOW}error: while running fastfetch {ANSI.RESET}", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
    except json.JSONDecodeError:
        print(f"{ANSI.YELLOW}error: couldn't parse fastfetch json.{ANSI.RESET}", file=sys.stderr)
    return None
