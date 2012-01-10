# A plugin that adds the /link command, letting you open links that are pasted
# in the conversation, without having to click them.

import os
import re

from plugin import BasePlugin, PluginConfig
from xhtml import clean_text, get_body_from_message_stanza
import common

url_pattern = re.compile(r'\b(http[s]?://(?:\S+))\b', re.I|re.U)

class Plugin(BasePlugin):
    def init(self):
        self.add_event_handler('private_msg', self.on_private_msg)
        self.add_event_handler('conversation_msg', self.on_conversation_msg)

    def on_private_msg(self, message, tab):
        fro = message['from']
        self.do_notify(message, fro)

    def on_conversation_msg(self, message, tab):
        fro = message['from'].bare
        self.do_notify(message, fro)

    def do_notify(self, message, fro):
        body = clean_text(get_body_from_message_stanza(message))
        if not body:
            return
        command = self.config.get('command', '').strip()
        if not command:
            self.core.information('No notification command was provided in the configuration file', 'Warning')
            return
        self.core.exec_command(command % {'body':body, 'from':fro})
