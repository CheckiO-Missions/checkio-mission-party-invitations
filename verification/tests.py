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
        prepare_test(middle_code='''party = Party()
nick = Friend('Nick')
john = Friend('John')
lucy = Friend('Lucy')
party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.del_friend(nick)''',
                     test="party.send_invites('Friday, Midnight Pub, 9:00 PM')",
                     answer='''John has been invited to the party: Friday, Midnight Pub, 9:00 PM
Lucy has been invited to the party: Friday, Midnight Pub, 9:00 PM''')
    ],
    "2. Second": [
        prepare_test(middle_code='''party = Party()
jack = Friend('Jack McConnel')
bob = Friend('Bob Monteu')
mary = Friend('Mary Forest')
party.add_friend(jack)
party.add_friend(bob)
party.add_friend(mary)''',
                     test="party.send_invites('Sunday, Karl`s home, 11:30 AM')",
                     answer='''Jack McConnel has been invited to the party: Sunday, Karl`s home, 11:30 AM
Bob Monteu has been invited to the party: Sunday, Karl`s home, 11:30 AM
Mary Forest has been invited to the party: Sunday, Karl`s home, 11:30 AM''')
    ],
    "3. Third": [
        prepare_test(middle_code='''party = Party()
karl = Friend('Karl')
rachel = Friend('Rachel')
wanda = Friend('Wanda')
party.add_friend(karl)
party.add_friend(wanda)''',
                     test="party.send_invites('Saturday, South entrance of the Yosemite, 7:00 AM')",
                     answer='''Karl has been invited to the party: Saturday, South entrance of the Yosemite, 7:00 AM
Wanda has been invited to the party: Saturday, South entrance of the Yosemite, 7:00 AM''')
    ],
    "4. Fourth": [
        prepare_test(middle_code='''party = Party()
patrick = Friend('Patrick')
amanda = Friend('Amanda')
grace = Friend('Grace')
party.add_friend(patrick)
party.add_friend(amanda)
party.add_friend(grace)''',
                     test="party.send_invites('Friday, Miranda`s home, 19:00')",
                     answer='''Patrick has been invited to the party: Friday, Miranda`s home, 19:00
Amanda has been invited to the party: Friday, Miranda`s home, 19:00
Grace has been invited to the party: Friday, Miranda`s home, 19:00''')
    ],
    "5. Fifth": [
        prepare_test(middle_code='''party = Party()
nick = Friend('Nick')
john = Friend('John')
lucy = Friend('Lucy')
party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.del_friend(nick)
party.del_friend(john)
party.del_friend(lucy)''',
                     test="party.send_invites('Sunday, Central Park, 14:20')",
                     answer="")
    ]

}
