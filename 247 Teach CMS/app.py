class ContactManagementSystem:
    def __init__(self):
        self.cms_network = {}
        self.cms_contacts = {}

    def addContact(self, contact_id, contact_name, contact_email, contact_number):
        # Adding contacts
        if contact_id not in self.cms_network:
            self.cms_network[contact_id] = (contact_name, contact_email, contact_number)
            self.cms_contacts[contact_id] = set()

    def deleteContact(self, contact_id):
        # Remove contacts as well as their friendships
        if contact_id in self.cms_network:
            del self.cms_network[contact_id]

    def addFriendship(self, contact_id1, contact_id2):
        # Create a friendship between two members
        if contact_id1 in self.cms_network and contact_id2 in self.cms_network:
            self.cms_contacts[contact_id1].add(contact_id2)
            self.cms_contacts[contact_id2].add(contact_id1)

    def reccomendFriends(self, friend_id):
        # Recommends friends for contacts (friends of friends)
        friend_recommendations = set()
        if friend_id in self.cms_contacts:
            friends = self.cms_contacts[friend_id]
            for friend in friends:
                friends_of_friend = self.cms_contacts[friend]
                friend_recommendations.update(friends_of_friend)
            # Remove the contact and their direct friends from recommendations
            friend_recommendations.discard(friend_id)
            friend_recommendations.difference_update(friends)
        return friend_recommendations

    def search(self, contact_name):
        # Search for a contact by name and return their ID
        for contact_id, name in self.cms_network.items():
            if name[0] == contact_name:
                return contact_id
        return None  # Contact not found

    def inOrderTraversal(self):
        # Print all of the contacts in alphabetical order
        for contact_id, contact_info in sorted(self.cms_network.items(), key=lambda x: x[1][0]):  # Sort by contact name
            print(f"Contact ID: {contact_id}")
            print(f"Name: {contact_info[0]}")
            print(f"Email: {contact_info[1]}")
            print(f"Phone Number: {contact_info[2]}")
            print()

if __name__ == "__main__":
    # Contacts
    cms = ContactManagementSystem()

    # Add contacts
    cms.addContact(1, "Mary Warren", "marywarren@gmail.com", "412-821-9394")
    cms.addContact(2, "John Hale", "halejohn@gmail.com", "800-102-3923")
    cms.addContact(3, "John Proctor", "proctorJ@outlook.com", "724-914-2232")
    cms.addContact(4, "Jay Brown", "jaybrown@yahoo.com", "412-914-0093")

    # Friendships
    cms.addFriendship(1, 2)
    cms.addFriendship(2, 3)
    cms.addFriendship(3, 4)

    # Contact Search
    contact_id = cms.search("Mary Warren")
    if contact_id:
        print(f"Contact found with ID: {contact_id}")

    contact_id = cms.search("John Hale")
    if contact_id:
        print(f"Contact found with ID: {contact_id}")

    contact_id = cms.search("John Proctor")
    if contact_id:
        print(f"Contact found with ID: {contact_id}")

    contact_id = cms.search("Jay Brown")
    if contact_id:
        print(f"Contact found with ID: {contact_id}")

    # Friend Recommendations
    friend_recommendations = cms.reccomendFriends(1)
    print("Friend recommendations for Mary Warren:", friend_recommendations)

    friend_recommendations = cms.reccomendFriends(3)
    print("Friend recommendations for John Hale:", friend_recommendations)

    # Print all contacts in alphabetical order
    cms.inOrderTraversal()
