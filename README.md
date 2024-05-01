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


## Step-by-step solution

### Install Evans
1. Download from https://github.com/ktr0731/evans/releases
2. Unzip
   ```
   tar xvf evans_linux_amd64.tar.gz
   ```
3. Move binary
   ```
   sudo mv evans /usr/local/bin
   ```

### Create users
1. Create a burner email on https://temp-mail.org/
2. Run evans in the proto/ directory
   ```
   evans --proto auth_service.proto --host <url> --port <port>
   ```
3. Create user
   ```
   > call SignUpUser
   ```
   An email will be sent to the previously email the user registered
4. Get verification code from email, and run
   ```
   > call VerifyEmail
   ```
5. Repeat twice
6. Store user data for later use in an json file

### Convert .proto files to .py
Run from project's root dir
```
python -m grpc_tools.protoc \
   --proto_path=./proto \
   --grpc_python_out=./src/proto_py \
   --python_out=./src/proto_py \
   ./proto/*.proto
```

### Run a sanity check
To check if connection to the server is available. Run the script from the directory src/:
```
python3 sanity_check.py
```

### Test user sign-in vacancy handler
```
python3 grpc_handlers.py
```

### Run locust tests
```
locust --headless --users 3 --run-time 5m
``````