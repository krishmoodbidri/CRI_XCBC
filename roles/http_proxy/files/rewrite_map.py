#!/usr/bin/env python3
import grp
import sys
import rewrite_map_config as cfg

while sys.stdin:
    hostname = ""
    try:
        username = sys.stdin.readline().strip()   ## It is very important to use strip!
        if username:
            for group in cfg.target_groups:
                if username in grp.getgrnam(group).gr_mem:
                    hostname = cfg.target_groups[group]
                    break

        if not hostname:
            hostname = cfg.default_hostname

    except:
        hostname = cfg.default_hostname

    print(hostname)
    sys.stdout.flush()
