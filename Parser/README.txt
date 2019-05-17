This parser is used to extract Finnish historical letters.

The design of this letter parser is based on English emails. 

How to used the parser in python

>>> import EFZP as zp
>>> p = zp.parse("hei kaikki, tama on testi, terveisin Juha")
>>> print p
{'salutation': 'hei kaikki, ', 'body': 'tama on testi, ', 'reply_text': None, 'signature': 'terveisin boyang'}
>>>
