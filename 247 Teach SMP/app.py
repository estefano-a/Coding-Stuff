class SocialNetwork:
    def __init__(self):
        # Initialize an empty network represented by a dictionary
        self.network = {}
        self.friendships = {}  # To store friendships

    def add_member(self, member_id, member_name):
        # Add a new member to the network
        if member_id not in self.network:
            self.network[member_id] = member_name
            self.friendships[member_id] = set()

    def delete_member(self, member_id):
        # Remove a member from the network and dissolve friendships
        if member_id in self.network:
            del self.network[member_id]
            del self.friendships[member_id]
            # Remove the member from the friendships of other members
            for friend_id in self.friendships:
                self.friendships[friend_id].discard(member_id)

    def establish_friendship(self, member_id1, member_id2):
        # Establish a friendship between two members
        if member_id1 in self.network and member_id2 in self.network:
            self.friendships[member_id1].add(member_id2)
            self.friendships[member_id2].add(member_id1)

    def dissolve_friendship(self, member_id1, member_id2):
        # Dissolve a friendship between two members
        if member_id1 in self.network and member_id2 in self.network:
            self.friendships[member_id1].discard(member_id2)
            self.friendships[member_id2].discard(member_id1)

    def member_search(self, member_name):
        # Search for a member by name and return their ID
        for member_id, name in self.network.items():
            if name == member_name:
                return member_id
        return None  # Member not found

    def friend_recommendations(self, member_id):
        # Get friend recommendations for a member (friends of friends)
        recommendations = set()
        if member_id in self.network:
            friends = self.friendships[member_id]
            for friend in friends:
                friends_of_friend = self.friendships[friend]
                recommendations.update(friends_of_friend)
            # Remove the member and their direct friends from recommendations
            recommendations.discard(member_id)
            recommendations.difference_update(friends)
        return recommendations

if __name__ == "__main__":
    # Social Network
    social_network = SocialNetwork()

    # Add members
    social_network.add_member(1, "John")
    social_network.add_member(2, "Alice")
    social_network.add_member(3, "Bob")
    social_network.add_member(4, "Charlie")

    # Friendships
    social_network.establish_friendship(1, 2)
    social_network.establish_friendship(2, 3)
    social_network.establish_friendship(3, 4)

    # Member Search
    member_id = social_network.member_search("John")
    if member_id:
        print(f"Member found with ID: {member_id}")

    member_id = social_network.member_search("Bob")
    if member_id:
        print(f"Member found with ID: {member_id}")

    member_id = social_network.member_search("Alice")
    if member_id:
        print(f"Member found with ID: {member_id}")

    # Friend recommendations
    recommendations = social_network.friend_recommendations(1)
    print("Friend recommendations for John:", recommendations)

    recommendations = social_network.friend_recommendations(3)
    print("Friend recommendations for Bob:", recommendations)