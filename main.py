#! python3
# mclip.py - A multi-clipboard program.
'''
input the keyword of bureaucratic response(官僚回應)
then copy the bureaucratic response to clipboard
use to reply line, e-mail, etc.
'''

import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


keyphrase = 's'
flag1 = True
while flag1:
    keyphrase = input('choose agree, busy, upsell:')

    if keyphrase == 'agree':
        flag1 = False
    elif keyphrase == 'busy':
        flag1 = False
    elif keyphrase == 'upsell':
        flag1 = False


print('pass')
pyperclip.copy(TEXT[keyphrase])
print('Text for ' + keyphrase + 'copied to clipboard.')
