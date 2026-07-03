# Contributing to Priup

First off, thank you for taking the time to contribute! We welcome contributions from everyone—whether you're fixing a bug, designing a new feature, writing documentation, or improving test coverage.

The following guidelines outline our development process and standards to ensure smooth collaboration.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Branching & Git Workflow](#branching--git-workflow)
4. [Local Development Setup](#local-development-setup)
5. [Commit Message Style Guide](#commit-message-style-guide)
6. [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project and everyone participating in it is governed by the [Priup Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## How Can I Contribute?

### Reporting Bugs
If you find a bug, please check the existing issues first. If it's a new issue, open a bug report using our [Bug Report Template](.github/ISSUE_TEMPLATE/1_bug_report.yml). Provide a clear description, reproduction steps, expected behavior, and environment details.

### Suggesting Enhancements
We love new ideas! If you have a feature suggestion, submit it using the [Feature Request Template](.github/ISSUE_TEMPLATE/2_feature_request.yml). Explain what problem it solves and suggest a possible implementation.

---

## Branching & Git Workflow

We follow a structured branching flow to keep our codebase stable:

* **`main`**: Represents the latest stable, production-ready release.
* **`development`**: The integration branch for active development. **All feature branches must branch off `development` and merge back into `development`.**

### Git Branching Workflow
1. Fetch the latest changes:
   ```bash
   git checkout development
   git pull origin development
   ```
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   # OR for bug fixes
   git checkout -b bugfix/your-fix-name
   ```
3. Commit and push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

---

## Local Development Setup

To configure Priup on your local machine:

1. Clone the project and initialize dependencies. Detailed setup instructions for Python and Node.js can be found in [docs/development.md](docs/development.md).
2. Install standard linters and formatters to match the codebase styling. See [docs/coding_standards.md](docs/coding_standards.md).
3. Verify your setup by running existing tests in the `tests/` directory:
   * Node tests: `npm test`
   * Python tests: `pytest`

---

## Commit Message Style Guide

We appreciate clear, readable commit messages. Please format your commit messages as follows:

```text
Type: Short summary under 50 characters (capitalized, no period)

A more detailed body explaining the "why" and "what" of your changes. Keep
lines wrapped at 72 characters.

Fixes #123
```

**Common Types:**
* `feat`: A new user-facing feature.
* `fix`: A bug fix.
* `docs`: Documentation updates.
* `style`: Code style changes (formatting, missing semi-colons, no logic change).
* `refactor`: Code changes that neither fix bugs nor add features.
* `test`: Adding missing tests or correcting existing tests.
* `chore`: Build steps, dependencies, tool configurations.

---

## Pull Request Process

1. **Target Branch:** Always target the `development` branch when opening a PR.
2. **Template:** Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) completely.
3. **Tests:** Ensure all automated checks (linters, type-checkers, unit tests) pass locally.
4. **Docs:** Update documentation if your change introduces new behavior or changes configurations.
5. **Review:** Assign a reviewer and respond to feedback. Once approved, a maintainer will merge the PR.
