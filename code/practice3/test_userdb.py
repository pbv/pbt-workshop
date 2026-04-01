# ------------------------------------------------------------------
# State machine testing the UserDB class
#
# Pedro Vasconcelos, 2025
# ------------------------------------------------------------------
from userdb import UserDB
from hypothesis import assume, settings, strategies as st
from hypothesis.stateful import RuleBasedStateMachine, \
    rule, precondition

# For faster testing
# settings.register_profile("fast", max_examples=50, stateful_step_count=20)
# settings.load_profile("fast")

class UserDBStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.db = UserDB() # start with an empty DB and model
        self.model = []  

    def teardown(self):
        self.db.close()

    users = st.integers(min_value=1, max_value=10)
    emails = st.emails()
        
    @rule(user=users, email=emails)
    def add(self, user, email):
        # update the implementation
        self.db.add(user, email)
        # update the mode
        if (user,email) not in self.model:
            self.model.append((user,email))

    @rule(user=users)
    def get(self, user):
        # query the implementation
        answer = self.db.get(user)
        # query the model
        expect = [email for (other,email) in self.model
                  if other==user]
        # postcondition        
        assert answer == expect

    @precondition(lambda self: self.model != [])
    @rule(user=users, email=emails)
    def remove(self, user, email):
        # precondition
        assume((user,email) in self.model)
        # update the implementation
        self.db.remove(user,email)
        # update the model
        self.model.remove((user,email))
        
    @rule(user=users)
    def delete(self,user):
        # update the implementation
        self.db.delete(user)
        # update the model
        self.model = [(other,email) for (other,email)
                      in self.model if other!=user]

Test = UserDBStateMachine.TestCase
