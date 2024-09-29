# Evan_Li_Mini1

[CI] https://github.com/nogibjj/Evan_Li_Mini1/actions/runs/10746169698

```
- Makefile
- requirements.txt
- main.py
- test_main.py
- mylib
    - test_main.py
- .github/workflows
    - cicd.yml
- .devcontainer
    - devcontainer.json
    - Dockerfile
- README.md
```

Usage:

1. Use make install (assuming this command is defined in the Makefile) to install dependencies.
2. Run tests to ensure everything is working correctly: make all or make test
3. You can set up the development environment using VS Code and .devcontainer.
4. When developing new features, add code in main.py or mylib/, and add corresponding tests in the appropriate test files.
5. When committing changes, the CI/CD pipeline will run automatically (as defined in .github/workflows/cicd.yml).
