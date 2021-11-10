from otree.models import Session

s = Session.objects.all()
for i in s:
    print(i.code)

