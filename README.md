# Awesome Codeql [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of CodeQL resources.

## Contents

- [Getting Started](#getting-started)
- [Tooling & Environment](#tooling--environment)
- [GitHub Actions & CI/CD](#github-actions--cicd)
- [Customization & Query Development](#customization--query-development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Getting Started

Resources for learning CodeQL, from beginner guides to official documentation.


### CodeQL Getting Started and Guides (along side the [official docs](https://codeql.github.com/docs/))

- [CodeQL Learning Catalog](https://codeql-learning-catalog.github.com/) - The CodeQL Learning Catalog is a resource dedicated providing detailed CodeQL learning resources. The Catalog contains workshops, recordings, and learning paths for improving your knowledge and skill in using CodeQL.
- [GitHub Security Lab](https://securitylab.github.com/get-involved/) - From trying out CodeQL to secure your own code to collecting bug bounties by securing others', here are a few ways we can keep the world's software safe, together.
- [testing-handbook](https://github.com/trailofbits/testing-handbook) - The [Trail of Bits Testing Handbook](https://appsec.guide/docs/static-analysis/codeql/) is a resource that guides developers and security professionals in configuring, optimizing, and automating many of the static and dynamic analysis tools used at Trail of Bits.
- [ReadMe Project - CodeQL Query Writing](https://github.com/readme/guides/custom-codeql-queries) - A beginner’s guide to running and managing custom CodeQL queries

### Documentation

- [How to write CodeQL Queries](https://codeql.github.com/docs/writing-codeql-queries)
- [CodeQL Language Guide](https://codeql.github.com/docs/codeql-language-guides)
- [QL Language reference](https://codeql.github.com/docs/ql-language-reference)
- [CodeQL Standard Libraries](https://codeql.github.com/codeql-standard-libraries)
- [CodeQL Query Help](https://codeql.github.com/codeql-query-help)
- [Full CodeQL Documentation](https://codeql.github.com/docs/)
- [CodeQL Custom Configuration File](https://gist.github.com/bthomas2622/e520926b88ebb93e79b30f7f32ed4849)


### Blogs

- [GitHub - CodeQL zero to hero series](https://github.blog/developer-skills/github/codeql-zero-to-hero-part-1-the-fundamentals-of-static-analysis-for-vulnerability-research/)
- [GitHub - How GitHub uses CodeQL to secure GitHub](https://github.blog/engineering/how-github-uses-codeql-to-secure-github/)

### YouTube learning

- [Find bugs in your code with CodeQL](https://www.youtube.com/live/y_-pIbsr7jc?&t=310)
- [Finding security vulnerabilities in JavaScript with CodeQL](https://www.youtube.com/watch?v=pYzfGaLTqC0)
- [Finding security vulnerabilities in Java with CodeQL](https://www.youtube.com/watch?v=nvCd0Ee4FgE)
- [Finding security vulnerabilities in C/C++ with CodeQL](https://www.youtube.com/watch?v=eAjecQrfv3o&t=98s)
- [CodeQL as an Audit Oracle](https://www.youtube.com/watch?v=-bJ2Ioi7Icg&t=8s)

---

## Tooling & Environment

Everything you need to install, run, and view CodeQL results locally or in containers.

### CodeQL Installers

- [GH CodeQL](https://github.com/github/gh-codeql) - GitHub CLI Extension for CodeQL to help manage installation
- [grab_ql](https://github.com/advanced-security/grab_ql) - Grab some/all of CodeQL CLI binary, QL library, VSCode starter workspace, VSCode and VSCode QL extension
- [codeql-anywhere](https://github.com/david-wiggs/codeql-anywhere) - Put the power of CodeQL in your pocket, take it with you to any CI 🚀
- [codeql-jupyter-kernel](https://github.com/GitHubSecurityLab/codeql-jupyter-kernel) - Jupyter Kernel for CodeQL
- [homebrew-cask](https://github.com/Homebrew/homebrew-cask/blob/master/Casks/c/codeql.rb) - Homebrew cask to install the CodeQL CLI `brew install --cask codeql`

### CodeQL CLI Tooling

- [gh-codeql](https://github.com/github/gh-codeql) - GitHub CLI extension for working with CodeQL
- [gh-codeql-scan](https://github.com/advanced-security/gh-codeql-scan) - GH CLI CodeQL Scan Extension
- [gh-mrva](https://github.com/GitHubSecurityLab/gh-mrva) - Multi-repo variant analysis CLI support

### CodeQL Containers

- [codeql-docker](https://github.com/advanced-security/codeql-docker) - CodeQL Docker image
- [codeql-container](https://github.com/microsoft/codeql-container) - Prepackaged and precompiled github codeql container for rapid analysis, deployment and development.
- [codeql_container_example](https://github.com/advanced-security/codeql_container_example) - Example showing CodeQL to scan containerized applications in GitHub Actions.
- [codeql-container-builds](https://some-natalie.dev/blog/codeql-container-builds/) - Blog walking through the complexities of implementing containerized CodeQL workloads sprinkled with bits of Kubernetes wisdom.

### CodeQL SARIF

- [Visual Studio SARIF Viewer](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) - Visual Studio Static Analysis Results Interchange Format (SARIF) log file viewer
- [VSCode SARIF Viewer](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer) - Adds support for viewing SARIF logs in Visual Studio Code
- [IntelliJ SARIF Viewer](https://plugins.jetbrains.com/plugin/23159-sarif-viewer)
- [SARIF Viewer Web Component](https://microsoft.github.io/sarif-web-component/)
- [psastras/sarif-rs-sarif-fmt](https://github.com/psastras/sarif-rs/tree/main/sarif-fmt) - This crate provides a command line tool to pretty print SARIF files to easy human readable output.

### CodeQL AI & LLM Tooling
- [GitHub Seclab Taskflow Agent](https://github.com/GitHubSecurityLab/seclab-taskflow-agent) - The framework includes a [CodeQL](https://codeql.github.com/) MCP server that can be used for Agentic code review, see the [CVE-2023-2283](examples/taskflows/CVE-2023-2283.yaml) taskflow for an example of how to have an Agent review C code using a CodeQL database ([demo video](https://www.youtube.com/watch?v=eRSPSVW8RMo)).
- [GitHub CodeQL Development MCP Server](https://github.com/github/codeql-development-mcp-server) - An MCP server supporting LLM requests for CodeQL development tools and resources.
- [codeql-development-template](https://github.com/advanced-security/codeql-development-template) - Copilot-native repository template for CodeQL query development. Lowering the barrier to entry for CodeQL development through natural language and GitHub Copilot. A GitHub repository template for building custom CodeQL queries with AI assistance. This template provides a structured environment with prompts, instructions, and workflows designed to guide GitHub Copilot Coding Agent through the complete CodeQL development lifecycle.


---

## GitHub Actions & CI/CD

Tools, actions, and examples for integrating CodeQL into your automation pipelines.

- [sample-pipeline-files](https://github.com/advanced-security/sample-codeql-pipeline-config) - This repository contains pipeline files for various CI/CD systems (AWS CodeBuild, Azure Devops, CircleCI, DroneCI, Jenkins, Tekton, Travis), illustrating how to integrate the CodeQL CLI Bundle for Automated Code Scanning

### CodeQL GitHub Actions Helpers

- [set-codeql-language-matrix](https://github.com/advanced-security/set-codeql-language-matrix) - Automatically set the CodeQL matrix job using the languages in your repository.
- [filter-sarif](https://github.com/advanced-security/filter-sarif) - GitHub Action for filtering Code Scanning alerts by path and id
- [sarif-toolkit](https://github.com/advanced-security/sarif-toolkit/blob/main/submodules/) - Allows users to split up SARIF files that use submodules into multiple SARIF files that are then published to there appropriate repositories.
- [codeql-debug](https://github.com/zbazztian/codeql-debug) - Add this action to an existing CodeQL analysis workflow to generate an html report
- [dismiss-alerts](https://github.com/advanced-security/dismiss-alerts) - Dismisses GitHub Code Scanning alerts from `//codeql[supress reason]` style comments on the default branch
- [adjust-cvss](https://github.com/advanced-security/adjust-cvss) - Adjust the severity of the CVSS score assigned to a result in SARIF file
- [codeql-sarif-security-standard-annotator](https://github.com/advanced-security/codeql-sarif-security-standard-annotator) - Add an `owasp-top10-2021` tag to relevant results
- [delombok](https://github.com/advanced-security/delombok) - Delombok Java Code for analysis with Code Scanning (deprecated - now [supported by CodeQL](https://github.blog/changelog/2023-09-01-code-scanning-with-codeql-improves-support-for-java-codebases-that-use-project-lombok/))
- [badge-generator](https://github.com/MichaelCurrin/badge-generator) - [![CodeQL](https://github.com/MichaelCurrin/badge-generator/workflows/CodeQL/badge.svg)](https://github.com/MichaelCurrin/badge-generator/actions?query=workflow%3ACodeQL "Code quality workflow status") Magically generate Markdown badges for your docs 🛡️ 🦡 🧙
- [monorepo-code-scanning-action](https://github.com/advanced-security/monorepo-code-scanning-action) - Focus SAST scans (with CodeQL) on just the changed parts of your monorepo, split up as you define
- [codeql-extractor-action](https://github.com/advanced-security/codeql-extractor-action) - An Action that allows you to specify a CodeQL extractor to be used in your workflows as an author of an Extractor.

### CodeQL Monorepo Actions Samples

- [parallel-code-scanning](https://github.com/dassencio/parallel-code-scanning) - An example of a GitHub Actions workflow showing how code scanning with CodeQL can be parallelized on monorepos.
- [multi-lang-monorepo](https://github.com/thedave42/multi-lang-monorepo) - A repo that demonstrates using an Actions workflow Job matrix to run parallel CodeQL scans on applications in a monorepo.
- [sample-javascript-monorepo](https://github.com/advanced-security/sample-javascript-monorepo) - Detached fork of babel/babel to use as a TypeScript monorepo sample with 150+ packages using the [monorepo-code-scanning-action](https://github.com/advanced-security/monorepo-code-scanning-action)

### CodeQL Enforcement

- [advanced-security-enforcer](https://github.com/zkoppert/advanced-security-enforcer) - A GitHub action for organizations that enables advanced security code scanning on all new repos
- [codeql-selective-analysis](https://github.com/octodemo/codeql-selective-analysis) - Make CodeQL a required status check for Pull Requests, but to skip the analysis in the case that only a certain subset of files are modified




---

## Customization & Query Development

Resources for extending CodeQL, creating packs, and using custom queries.

### CodeQL [Packs](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/publishing-and-using-codeql-packs)

- [GitHub-maintained packages](https://github.com/orgs/codeql/packages)
- [GitHub Security Lab community](https://github.com/GitHubSecurityLab/CodeQL-Community-Packs) - Collection of community-driven CodeQL query, library and extension [packages](https://github.com/orgs/githubsecuritylab/packages). Blog: [Announcing CodeQL Community Packs](https://github.blog/security/vulnerability-research/announcing-codeql-community-packs/)
- Trail of Bits - [codeql-queries](https://github.com/trailofbits/codeql-queries) - CodeQL queries and [packs](https://github.com/orgs/trailofbits/packages?ecosystem=all&q=repo%3Atrailofbits%2Fcodeql-queries) developed by Trail of Bits
- [GitHub codeql-coding-standards](https://github.com/github/codeql-coding-standards) - This repository contains CodeQL queries and libraries which support various Coding Standards. (AUTOSAR C++, CERT-C++,CERT C, MISRA C)

### CodeQL Tooling (Bundles + Packs)

- [codeql-bundle-action](https://github.com/advanced-security/codeql-bundle-action) - Action to retrofit a CodeQL bundle with additional queries, libraries, and customizations
- [codeql-bundle](https://github.com/rvermeulen/codeql-bundle) - CLI to build a custom CodeQL bundle
- [gh-tailor](https://github.com/zbazztian/gh-tailor) - A tool for customizing CodeQL packs.

### CodeQL Libraries & Utilities
- [codeql-qtil](https://github.com/advanced-security/codeql-qtil) - A library with a wide variety of handy CodeQL utilities, from simple to complex.

### Custom Modeling
- [codeql-summarize](https://github.com/advanced-security/codeql-summarize) - CodeQL Summary Generator to generate Models as Data (MaD) from CodeQL databases.
- [GitHub Security Lab models](https://github.com/GitHubSecurityLab/CodeQL-Community-Packs/blob/main/configs/default.yml#L19-L25)
- [Ex: Python Pickle](https://github.com/octodemo/vulnerable-pickle-app/blob/main/custom-queries/python/dangerous-functions.ql) - mapping a custom framework in python

### CodeQL Queries/Bundles

- [Microsoft solorigate queries](https://www.microsoft.com/en-us/security/blog/2021/02/25/microsoft-open-sources-codeql-queries-used-to-hunt-for-solorigate-activity/)
- [GitHub codeql-coding-standards-bundle-releases](https://github.com/advanced-security/codeql-coding-standards-bundle-releases) - CodeQL bundles containing the CodeQL Coding Standards queries



### CodeQL Query Suites

- [Only Critical Queries sample .qls](https://github.com/zbazztian/only-critical-queries/blob/main/.github/critical-alternative.qls)
- [OWASP Top 10 CWE Only .qls](https://github.com/securingdev/codeql-query-suites/blob/main/.github/configurations/owasp-top-10.qls)
- [CodeQL per Suite Query list](https://github.com/github/codeql/actions/workflows/query-list.yml?query=branch%3Acodeql-cli%2Flatest) -  download the attached `code-scanning-query-list.csv` artifact. 


### CodeQL Extractors

- [codeql-extractor-iac](https://github.com/advanced-security/codeql-extractor-iac) - CodeQL Extractors, Library, and Queries for Infrastructure as Code ( Terraform / HCL, JSON, YAML, Container files, Bicep )
- [codeql-extractor-bicep](https://github.com/GitHubSecurityLab/codeql-extractor-bicep) - CodeQL Extractor for Bicep Configurations
- [codeql-kaleidoscope](https://github.com/aibaars/codeql-kaleidoscope/) - CodeQL for LLVM Kaleidoscope ([AST/CFG/SSA/Dataflow in separate commits](https://github.com/aibaars/codeql-kaleidoscope/commits/main/)) 
- [Powershell Extractor](https://github.com/microsoft/codeql/blob/main/powershell/README.md) - CodeQL extractor, sample queries, and tools for Powershell
- [CyScout Solidity Extractor](https://github.com/CoinFabrik/CyScout/tree/main/solidity/codeql) - Run queries and detect vulnerabilities in your smart contracts using CodeQL-Solidity
- [cobol-codeql](https://github.com/krisds/cobol-codeql) - Archive of CodeQL support for COBOL (This is a one-off release of code for supporting analysis of COBOL programs using QL. The release of this code does not imply any intention to support it in the future.)
- [codeql-extractor-action](https://github.com/advanced-security/codeql-extractor-action) - specify a CodeQL extractor to be used in your workflows as an author of an Extractor.


## Troubleshooting

- [CodeQL Build Failure Troubleshooting](https://github.com/advanced-security/advanced-security-material/tree/main/troubleshooting/codeql-builds)
- [GitHub SARIF Upload Troubleshooting](https://github.com/advanced-security/advanced-security-material/blob/main/troubleshooting/sarif-upload/troubleshooting.md)
- [CodeQL Coding Standards - Hazard and risk analysis](https://github.com/github/codeql-coding-standards/blob/main/docs/user_manual.md#hazard-and-risk-analysis) 


## Contribute

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## Why

[What is an awesome list?](https://github.com/sindresorhus/awesome/blob/main/awesome.md)
