# wally

## Using

```
poetry add wally
```

## Developing

```
poetry install
```

## Scripts

A number of common checks and tools have been wired up with poetry scripts. Here are some examples

### Linting
```
poetry run lint  # will run the linter checks configured for this project
```

### Testing
```
poetry run test  # run unit tests uning the testing framworks configured for this project
```

### Format checking
```
poetry run format  # run a format checker configured for this project.
```

### All checks
There is also an easy way to run all of these checks at once:

```
poetry run qa  # run all checks
```

## Publishing

Publish by bumping the `version` in [pyproject.toml](pyproject.toml) and
committing to master (*e.g.*, via a PR merge).


# TODO's
- Define sceptre templates for launching AWS resources
  - For Jenkins master
    - EC2 instance
    - Install Jenkins
    - Install git
    - Install docker
    - Create docker group
    - Add Jenkins user to the docker group
    - Restart Jenkins service
