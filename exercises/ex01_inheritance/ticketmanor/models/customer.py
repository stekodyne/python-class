"""
Customer model class
"""

__author__ = 'Mike Woinoski mike@articulatedesign.us.com'

# TODO: import the User class from the ticketmanor.models.user module


# TODO: make Customer a subclass of User
class Customer:
    """
    Model class for Customer
    """

    def __init__(self, first_name, last_name, email, middles=None,
                 street=None, city=None, state=None, country=None,
                 post_code=None, customer_id=None):

        # TODO: call the superclass __init__() method, passing the
        # appropriate arguments
        # TODO: save any remaining arguments in data attributes of the
        # current Customer object

        # TODO: for any argument that you passed to the superclass constructor,
        # delete its attribute assignment from the next block of statements.
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.middles = middles
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.post_code = post_code
        self.customer_id = customer_id

    # TODO: copy all the methods below this comment and paste them into the
    # User class

    # TODO: Modify the methods here to reference Customer-specific attributes
    # when necessary, while delegating as much work as possible to superclass
    # methods.
    # HINT: you will be able to delete some methods completely; others can
    # override the superclass methods and then call the superclass methods to
    # do part of the work.
    # HINT: add a reference to self.customer_id to __eq__() and __repr__()

    def name(self):
        middle_name = self.middles + " " if self.middles is not None else ""
        return "{self.first_name} {}{self.last_name}"\
            .format(middle_name, self=self)

    def __eq__(self, other):
        """Compare Customer instances."""
        return isinstance(other, self.__class__) and \
            other.first_name == self.first_name and \
            other.middles == self.middles and \
            other.last_name == self.last_name and \
            other.email == self.email and \
            other.street == self.street and \
            other.city == self.city and \
            other.state == self.state and \
            other.country == self.country and \
            other.post_code == self.post_code

    def __ne__(self, other):
        """Compare Customer instances."""
        return not self.__eq__(other)

    def __str__(self):
        """Return a human-readable representation of a Customer"""
        return self.name + " " + self.email

    def __repr__(self):
        """Return an unambiguous String representation of a Customer"""
        return "id={self.id},first_name='{self.first_name}'," \
            "middles='{self.middles}',last_name='{self.last_name}'," \
            "email='{self.email}',street='{self.street}'," \
            "city='{self.city}',state='{self.state}'," \
            "country='{self.country}',post_code='{self.post_code}'," \
            .format(self=self)
