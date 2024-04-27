# MagicMedia dev challenge

## Task Description
Create a locust load testing script (https://docs.locust.io/en/stable/) that fetches vacancies from our vacancy server.

Our vacancy server is available at `url` and uses gRPC, you can find the proto definition of the server in attachment.

### Pre-requirements
Use [BloomRPC](https://github.com/bloomrpc/bloomrpc) or [Evans](https://github.com/ktr0731/evans)

1. Create 3 users on the server (SignUpUser)
2. Verify the email of the users (VerifyEmail)
3. Store the credentials somewhere for later use


### Load testing script flow

1. Every locust user should login with one of the user credentials created in pre-requirements.
2. In a recurring flow every locust user should execute the following actions every 30 seconds:
   a. Create a vacancy with pseudo-random data
   b. Update one or more fields in that vacancy
   c. Fetch that specific vacancy
   d. Delete the vacancy
3. In the background the locust user should fetch a list of all vacancies available on the server every 45 seconds.

Report the response times of the gRPC request in locust as well as any errors that would be returned by the gRPC server.
Please submit your resulting code in a zip or share a GitHub link.


## Additional comments
Run in the command line
locust --headless --users 10 --spawn-rate 1 -H http://your-server.com