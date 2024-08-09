# Substack Reverse Proxy

Built on the [Serverless Framework](https://www.serverless.com)

[Serverless Documentation](https://www.serverless.com/framework/docs/providers/aws/events/)

## Functionality
The `posts` function returns metadata about recent posts I've published.

## Usage

### Deployment

```
serverless deploy
```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```
serverless invoke --function posts
```

### Local development

```
serverless invoke local --function posts
```

### Dependencies

Since we're using the `requests` Python library, we need to add the `serverless-python-requirements` plugin

```
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
