# Falcon StatsD Example Application on Clever Cloud

[![Clever Cloud - PaaS](https://img.shields.io/badge/Clever%20Cloud-PaaS-orange)](https://clever-cloud.com)

This is a minimal Falcon application that demonstrates how to send custom business metrics via StatsD on Clever Cloud.

## About the Application

This application provides a simple HTTP endpoint:
- `/` - Returns a Grace Hopper quote and increments a StatsD counter (`hello_requests`)

## Technology Stack

- [Falcon](https://falconframework.org/) 4.x - A minimalist, high-performance Python web framework for building APIs
- [Gunicorn](https://gunicorn.org/) 23.x - A Python WSGI HTTP server for UNIX
- [StatsD](https://github.com/jsocol/pystatsd) 4.x - A simple StatsD client for Python
- Python 3.12+

## Prerequisites

- Python 3.12+
- pip

## Running the Application Locally

```bash
pip install -r requirements.txt
gunicorn server:app
```

The application will be accessible at http://localhost:8000.

## Deploying on Clever Cloud

You have two options to deploy your Falcon application on Clever Cloud: using the Web Console or using the Clever Tools CLI.

### Option 1: Deploy using the Web Console

#### 1. Create an account on Clever Cloud

If you don't already have an account, go to the [Clever Cloud console](https://console.clever-cloud.com/) and follow the registration instructions.

#### 2. Set up your application on Clever Cloud

1. Log in to the [Clever Cloud console](https://console.clever-cloud.com/)
2. Click on "Create" and select "An application"
3. Choose "Python" as the runtime environment
4. Configure your application settings (name, region, etc.)

#### 3. Configure Environment Variables

Add the following environment variables in the Clever Cloud console:

| Variable | Value | Description |
|----------|-------|-------------|
| `CC_PYTHON_MODULE` | `server:app` | WSGI module and application object |
| `CC_PYTHON_BACKEND` | `gunicorn` | WSGI server to use |

> **Note:** StatsD metrics are collected automatically on Clever Cloud. A StatsD server listens on port **8125** by default. You can query your metrics in the console under the **Metrics** tab using the `statsd.` prefix.

#### 4. Deploy Your Application

You can deploy your application using Git:

```bash
# Add Clever Cloud as a remote repository
git remote add clever git+ssh://git@push-par-clevercloud-customers.services.clever-cloud.com/app_<your-app-id>.git

# Push your code to deploy
git push clever master
```

### Option 2: Deploy using Clever Tools CLI

#### 1. Install Clever Tools

Install the Clever Tools CLI following the [official documentation](https://www.clever-cloud.com/doc/clever-tools/getting_started/):

```bash
# Using npm
npm install -g clever-tools

# Or using Homebrew (macOS)
brew install clever-tools
```

#### 2. Log in to your Clever Cloud account

```bash
clever login
```

#### 3. Create a new application

```bash
# Step 1: Initialize the current directory as a Clever Cloud application
clever create --type python <YOUR_APP_NAME>

# Step 2: Add your domain (optional but recommended)
clever domain add <YOUR_DOMAIN_NAME>

# Step 3: Set the required environment variables
clever env set CC_PYTHON_MODULE server:app
clever env set CC_PYTHON_BACKEND gunicorn
```

#### 4. Deploy your application

```bash
clever deploy
```

#### 5. Open your application in a browser

Once deployed, you can access your application at `https://<YOUR_DOMAIN_NAME>/`.

### Monitoring Your Application

Once deployed, you can monitor your application through:

- **Web Console**: The Clever Cloud console provides logs, metrics, and other tools to help you manage your application.
- **CLI**: Use `clever logs` to view application logs and `clever status` to check the status of your application.

## Additional Resources

- [Falcon Documentation](https://falcon.readthedocs.io/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [pystatsd Documentation](https://statsd.readthedocs.io/)
- [Clever Cloud Python Documentation](https://www.clever-cloud.com/developers/doc/applications/python/)
- [Clever Cloud Metrics](https://www.clever-cloud.com/developers/doc/metrics/)
