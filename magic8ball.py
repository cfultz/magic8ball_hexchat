from __future__ import print_function

from random import choice

import hexchat

__module_name__ = 'Magic 8 Ball Responses'
__module_version__ = '0.1'
__module_description__ = 'Displays random Magic 8 Ball responses for IRC users'
__author__ = 'Caleb Fultz (aka) cfultz (aka) sippycup (aka)'

magics = [
    'Signs point to yes, {}',
    'Yes, {}',
    'Reply hazy, try again.',
    'Without a doubt, {}',
    'My sources say no.',
    'Cannot predict now.',
    'As I see it, yes.',
    'Better not tell you now, {}',
    'Very doubtful.',
    'Concentrate and ask again, {}',
    'Don\'t count on it, {}',
    'Probably.',
    'Are you kidding, {}?',
    'Go for it, {}!'
]


def magic_cb(word, word_eol, userdata):
    if len(word) > 1:
        nick = word[1]
        hexchat.command('me shakes the Magic 8 Ball. It answers: ' + choice(magics).format(nick))
    else:
        hexchat.command('help magic8')
    return hexchat.EAT_ALL


def unload_cb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_command('magic', magic_cb, help='magic8 <nick>')
hexchat.hook_unload(unload_cb)
print(__module_name__, 'version', __module_version__, 'loaded.')
