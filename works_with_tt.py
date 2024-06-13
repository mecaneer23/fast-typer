#!/usr/bin/env python3
"""
Cheat on typing tests. This script works with tt (https://github.com/lemnos/tt).

To use this script, copy the text you want to type and paste it in quotes as
the first argument to this script.

```bash
python3 ./works_with_tt.py "example text goes          here"
```
"""

from time import sleep
from sys import argv

from pynput.keyboard import Controller


def main() -> None:
    """Entry point"""
    text = " ".join(argv[1].split())
    controller = Controller()
    sleep(3)
    for letter in text:
        controller.type(letter)


if __name__ == "__main__":
    main()
