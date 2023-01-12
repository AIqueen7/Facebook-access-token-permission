import facebook

def check_access_token_permissions(access_token):
    try:
        graph = facebook.GraphAPI(access_token)
        # Get the list of permissions associated with the token
        permissions = graph.request("/me/permissions")
        return permissions['data']
    except facebook.GraphAPIError as e:
        print(f"An error occurred: {e}")
        return None

access_token = "YOUR_ACCESS_TOKEN"
permissions = check_access_token_permissions(access_token)
if permissions:
    print("Access Token has the following permissions:")
    for permission in permissions:
        if permission['status'] == "granted":
            print("- " + permission['permission'])
else:
    print("An error occurred while checking the permissions of the Access Token.")