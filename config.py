APPNAME             = 'bot_id'
BASEURL             = 'https://_instance_'

FOLLOW              = "yourself"
PUBLIC_ONLY         = True
NO_REBLOG           = True
DATEFORMAT			= "%m/%d/%Y"
OUTPUT_JSON_FILE    = 'tl.json'

# TODO add caching options

# max number of statuses per fetch. There is no guarantee to fetch ALL from
# timeline if this number is set higher. As it also depends on the server side
# rate limit
LIMIT               = 40

# bot account username and password
# Priority: plaintext UNAME/PW in this config >  input at runtime
UNAME               = ""
PW                  = ""

# you don't need to modify these
CLIENTID = 'client.secret'
TOKEN = 'token.secret'

def get_secrets_from_input():
	print("account secret not found, please manually input: ")
	UNAME = input("username or email: ")
	PW = input("password (not concealed): ")
	return (UNAME, PW)


