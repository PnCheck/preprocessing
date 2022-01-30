Deployed to: https://preprocessing-pncheck.azurewebsites.net/

# Routes

### Root
	URL: /
	Method: GET
	Return: {"message":"Up and running!"}


### Prepare
	URL: /prepare
	Method: POST
	Data: {"file":file}
	Return: {"image":2dArray}