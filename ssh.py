# From tutorial: https://www.youtube.com/watch?v=AkcxJWbHV0w

from paramiko import SSHClient, AutoAddPolicy

class SSH_Manager:
    def __init__(self):
        self.client = SSHClient()

        self.client.load_system_host_keys("~/.ssh/known_hosts")
        self.client.set_missing_host_key_policy(AutoAddPolicy())