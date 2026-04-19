# DevSecOps Practice Pipeline

> ⚠️ **This repository contains intentionally vulnerable code for security testing and educational purposes.**

## Stack

| Tool | Purpose | Type |
|------|---------|------|
| Trivy | Container & dependency scanning | SCA |
| Semgrep | Static code analysis | SAST |
| GitLeaks | Secret detection | Secrets |
| OWASP ZAP | Dynamic application testing | DAST |
| SonarQube | Code quality & security | SAST |
| Syft | SBOM generation | Supply Chain |
| DefectDojo | Vulnerability aggregation | ASOC |

## Pipeline

### GitHub Actions
- Trivy, Semgrep, GitLeaks, Syft (SBOM)

### GitLab CI (self-hosted)
- Full pipeline with SonarQube + DefectDojo integration
- Two stages: `security` → `reporting`

## Infrastructure (self-hosted)
- GitLab CE
- Jenkins
- SonarQube
- DefectDojo
- All running via Docker Compose

## Vulnerable App
Flask application with intentional vulnerabilities:
- Command Injection (`/ping` endpoint)
- SQL Injection (`/user` endpoint)
- Hardcoded AWS credentials
- Weak hashing (MD5)
- Missing security headers (found by ZAP)

## Purpose
Practice environment for DevSecOps toolchain integration.
Each vulnerability is detected by the security pipeline and aggregated in DefectDojo.
