import dropbox

# Use the REFRESH_TOKEN obtained in Step 1
APP_KEY = ""
APP_SECRET = ""
SAVED_REFRESH_TOKEN = ""

# Initialize Dropbox object using the refresh token
# The SDK handles the token refresh automatically in the background

dbx = dropbox.Dropbox(
    app_key=APP_KEY,
    app_secret=APP_SECRET,
    oauth2_refresh_token=SAVED_REFRESH_TOKEN
)

try:
    # Example API call
    account_info = dbx.users_get_current_account()
    print("Successfully connected to Dropbox account: {account_info.name.display_name}")

    # You can now proceed with your production API calls,
    # and the SDK will manage the short-lived access tokens for you.

except dropbox.exceptions.AuthError as err:
    print("Authentication failed. Check your app key, app secret, and refresh token.")
    print(err)
except Exception as err:
    print(f"An error occurred: {err}")