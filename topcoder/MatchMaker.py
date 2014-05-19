#!/usr/bin/env python

__author__ = 'Rio'

class MatchMaker(object):
    """Find the best matcher."""

    def __init__(self):
        pass

    @staticmethod
    def getBestMatches(members, currentUser, sf):
        """Return best matched members list consisting of members' names who
        have at least sf identical answers to the current user and are of the
        request gender.

        *Approach
        * Filter out all desired gender users.
        * Find the matched sf based on requested user list.

        :param members(set) Users list contains name, gender, request gender and answers.
        :param currentUser(str) Current user's name
        :param sf(int) identical score
        """

        def get_score(member, current_user):
            score = 0
            for i in range(len(current_user)):
                if member[i] == current_user[i]:
                    score += 1
            return score

        def is_matched(member, current_user):
            return current_user[2] == member[1]

        current_user = []
        for member in members:
            user = member.split(" ")
            print member
            if user[0] == currentUser:
                current_user = user

        matches = []
        for member in members:
            user = member.split(" ")
            if is_matched(user, current_user) and get_score(user[3:], current_user[3:]) >= sf:
                if user[0] != current_user[0]:
                    matches.append(user[0])

        return matches


if __name__ == '__main__':
    test = {"BETTY F M A A C C",
            "TOM M F A D C A",
            "SUE F M D D D D",
            "ELLEN F M A A C A",
            "JOE M F A A C A",
            "EDD M F A D D A",
            "SALLY F M C D A B",
            "MARGE F M A A C C"}

    # If current user is 'Betty' and sf=2, TOM and JOE should be there
    #result = MatchMaker.getBestMatches(test, "BETTY", 2)
    #print result

    #result = MatchMaker.getBestMatches(test, "MARGE", 4)
    #print result

    #test2 = {"BOB M M A", "FRED M F A", "JIM F M A", "DAISY F F A"}
    test3 = {"BETTY F M A A C C", "TOM M F A D C A", "SUE F M D D D D", "ELLEN F M A A C A", "JOE M F A A C A", "ED M F A D D A", "SALLY F M C D A B", "MARGE F M A A C C"}
    result = MatchMaker.getBestMatches(test3, "JOE", 1)
    print result
