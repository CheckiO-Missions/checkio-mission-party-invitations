init_code = """
if not "Friend" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Friend'?")
Friend = USER_GLOBAL['Friend']

if not "Party" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Party'?")
Party = USER_GLOBAL['Party']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. First": [
        prepare_test(middle_code='''party = Party("Midnight Pub")
nick = Friend('Nick')
john = Friend('John')
lucy = Friend('Lucy')
party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invites('Friday, 9:00 PM')
party.del_friend(nick)
party.send_invites("Saturday, 10:00 AM")
''',
                     test="nick.show_invite()",
                     answer='Midnight Pub: Friday, 9:00 PM')
    ],
    "2. Second": [
        prepare_test(middle_code='''party = Party("Karl`s home")
jack = Friend('Jack McConnel')
bob = Friend('Bob Monteu')
mary = Friend('Mary Forest')
party.add_friend(jack)
party.add_friend(bob)
party.send_invites('Sunday, 11:30 AM')
party.add_friend(mary)''',
                     test="mary.show_invite()",
                     answer="No party...")
    ],
    "3. Third": [
        prepare_test(middle_code='''party = Party("South entrance of the Yosemite")
karl = Friend('Karl')
rachel = Friend('Rachel')
wanda = Friend('Wanda')
party.add_friend(karl)
party.add_friend(wanda)
party.send_invites('Saturday, 7:00 AM')''',
                     test="rachel.show_invite()",
                     answer="No party...")
    ],
    "4. Fourth": [
        prepare_test(middle_code='''party = Party("Miranda`s home")
patrick = Friend('Patrick')
amanda = Friend('Amanda')
grace = Friend('Grace')
party.add_friend(patrick)
party.add_friend(amanda)
party.add_friend(grace)
party.send_invites('Friday, 19:00')''',
                     test="grace.show_invite()",
                     answer="Miranda`s home: Friday, 19:00")
    ],
    "5. Fifth": [
        prepare_test(middle_code='''party = Party("Central Park")
nick = Friend('Nick')
john = Friend('John')
lucy = Friend('Lucy')
party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.del_friend(nick)
party.del_friend(john)
party.del_friend(lucy)
party.send_invites('Sunday, 14:20')''',
                     test="lucy.show_invite()",
                     answer="No party...")
    ]

}
