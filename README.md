# wally

## Using

```
poetry add your-project
```

## API Specification for your-project

It is highly recomended to outline the interface for utilizing your package.

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
