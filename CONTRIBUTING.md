# Contributing

A script that ranks Kennel Club dog breeds by Levenshtein distance from a name.

Bug reports and feature requests are welcome as [issues](https://github.com/maubergine/dog-levenshtein/issues). Pull requests are
welcome too; CI on a pull request from a fork may wait for the maintainer to approve it.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/): `fix:`, `feat:`, `chore:`, `docs:` and so on. They
decide the next version: `fix` releases a patch, `feat` a minor version, and a breaking change a major one. CI checks
every commit (`commitlint.yml`). To check them locally before you push:

```sh
npm install   # installs commitlint and turns on .githooks/commit-msg
```

Commits to `main` must be signed.

## Tests

Install the dependencies with `pipenv install --deploy`, then run `pipenv run python -m py_compile dog-levenshtein.py`.
