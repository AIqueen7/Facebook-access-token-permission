# Facebook-access-token-permission

This code uses the facebook-sdk library to create a GraphAPI object using the given access token. It then makes a request to the '/me/permissions' endpoint, which returns the list of permissions associated with the authenticated user's token. It will then prints the list of granted permissions. If the request fails, it returns None.

It's important to note that some permissions are not available in the latest version of the API, so it's recommended to check the documentation for the version of the API you're using, and make sure you're requesting the correct permissions. Also, permissions can be granted, declined or expired, so make sure to check the status of each permission to know its current state.
