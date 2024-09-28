# Backend Repository Setup Guide

This guide provides step-by-step instructions to set up and run your backend repository. It covers running Docker Compose, installing dependencies, configuring environment variables, starting necessary services, and interacting with the API using Postman.

## Prerequisites

Ensure you have the following installed on your system:

- **Docker & Docker Compose**: [Install Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **Postman**: [Download Postman](https://www.postman.com/downloads/)

## Step 1: Clone the Repository

```bash
git clone https://github.com/vrs-darkness/Gamify-Works.git
cd Gamify-Works/backend/
```

## Step 2: Start Docker Services

First, run the Docker Compose file to set up necessary services like databases, caches, etc.

```bash
docker-compose up -d
```

- The `-d` flag runs the containers in detached mode.

## Step 3: Install Python Dependencies

Install the required Python packages listed in `requirements.py`.

> **Note:** Typically, dependencies are listed in a `requirements.txt` file. If your project uses `requirements.py`, ensure it contains a list of dependencies in the correct format.

```bash
pip install -r requirements.py
```

## Step 4: Configure Environment Variables

1. **Create a `.env` File:**

   A dummy `.env` file is provided (e.g., `.env.example` or `.env(dummy)`). Copy and rename it to `.env`.

   ```bash
   cp .env.example .env
   ```

   *Replace `.env.example` with `.env(dummy)` if applicable.*

2. **Populate the `.env` File:**

   Fill in the necessary keys with appropriate dummy values. Below is an example structure:

   ```env
    # Azure OpenAI Configuration
    AZURE_OPENAI_API_KEY=your_azure_openai_api_key
    AZURE_API_VERSION=2024-02-01
    AZURE_API_URL=https://your-azure-api-url.com
    AZURE_DEPLOYMENT_NAME=your_deployment_name
    # Database Configuration
    db_name=your_database_name
    db_user=your_database_user
    db_password=your_secure_password
    # Google API Configuration
    GOOGLE_API_KEY=your_google_api_key
    # Application Settings
    Time_Delay=30  # Time delay in seconds
    Key=your_secret_key
    Algo=HS256  # Algorithm used for token encoding
   ```

   > **Tip:** Replace the placeholder values with actual credentials or secure values as needed.

## Step 5: Start Celery Worker

Open a new terminal window/tab and navigate to your project directory. Start the Celery worker with the following command:

```bash
celery -A utils workers --loglevel=info
```

- **`-A utils`**: Specifies the Celery application module.
- **`--loglevel=info`**: Sets the logging level to info.

## Step 6: Start FastAPI Server

In another terminal window/tab, navigate to your project directory and start the FastAPI server using Uvicorn:

```bash
uvicorn API:app --reload
```

- **`API:app`**: Replace `API` with your FastAPI application's module name if different.
- **`--reload`**: Enables auto-reloading on code changes (useful for development).

> **Note:** Ensure that both Celery and FastAPI servers are running simultaneously.

## Step 7: Create a New User

With the servers running, you can now create a new user via the `/create/user` endpoint.

### Using CURL:

```bash
curl -X POST "http://localhost:8000/create/user" \
     -H "Content-Type: application/json" \
     -d '{
           "username": "string",
           "Name": "string",
           "Password": "string",
           "mail": "string"
         }'
```

### Using Postman:

1. **Open Postman** and create a new `POST` request.
2. **URL:** `http://localhost:8000/create/user`
3. **Headers:**
   - `Content-Type`: `application/json`
4. **Body:**
   - Select `raw` and `JSON` format.
   - Provide user details, for example:

     ```json
     {
       "username": "string",
       "Name": "string",
       "Password": "string",
       "mail": "string"
     }
     ```

5. **Send the Request** to create a new user.

## Step 8: Generate an Access Token

To authenticate and use the API services, generate an access token using the `/token` endpoint.

### Using CURL:

```bash
curl -X POST "http://localhost:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=your_username&password=your_password"
```

### Using Postman:

1. **Open Postman** and create a new `POST` request.
2. **URL:** `http://localhost:8000/token`
3. **Headers:**
   - `Content-Type`: `application/x-www-form-urlencoded`
4. **Body:**
   - Select `x-www-form-urlencoded`.
   - Add the following fields:
     - `username`: `your_username`
     - `password`: `your_password`
5. **Send the Request** to receive the access token.

> **Response Example:**

```json
{
  "access_token": "your_generated_token",
  "token_type": "bearer"
}
```

## Step 9: Use the API Services with Authentication

With the access token obtained, you can now interact with protected API endpoints.

### Steps to Use Postman with Authentication:

1. **Open Postman** and create a new request for the desired API endpoint.
2. **Select the HTTP method** (e.g., `GET`, `POST`, etc.) and enter the endpoint URL.
3. **Add Authentication Header:**
   - Navigate to the **Headers** tab.
   - Add a new header:
     - **Key:** `Authentication`
     - **Value:** `Bearer your_generated_token`

   > **Note:** The standard header for bearer tokens is `Authorization`. If your API expects `Authentication`, use that. Otherwise, consider using `Authorization`.

4. **Configure Request Details:**
   - Add necessary headers, parameters, or body as required by the endpoint.
5. **Send the Request** to interact with the API.

### Example: Accessing a Protected Endpoint

Assuming you have a protected endpoint at `/protected/resource`:

1. **Create a New Request** in Postman:
   - **Method:** `GET`
   - **URL:** `http://localhost:8000/protected/resource`
2. **Add Authentication Header:**
   - **Key:** `Authentication`
   - **Value:** `Bearer your_generated_token`
3. **Send the Request** to access the resource.

## Troubleshooting

- **Docker Issues:**
  - Ensure Docker is running.
  - Check container logs using `docker-compose logs`.

- **Dependency Installation Errors:**
  - Verify Python version.
  - Ensure all dependencies in `requirements.py` are correct.

- **Server Not Starting:**
  - Check for port conflicts.
  - Review logs for error messages.

- **Authentication Failures:**
  - Ensure the access token is valid and not expired.
  - Confirm the token is included correctly in the request headers.

## Conclusion

By following this guide, you should be able to set up and run your backend repository successfully. Utilize Postman to interact with your API endpoints securely using authentication tokens. For further assistance reach out to me.
