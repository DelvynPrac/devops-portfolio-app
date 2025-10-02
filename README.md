# Delvyn Jones • DevOps Portfolio (Flask microservice)

A production-style portfolio site implemented as a **DevOps practice project**:
- Flask microservice (5 pages: Home, About, Projects, Skills, Contact)
- CI/CD via **Jenkins** on EC2 → Docker → private registry → **EKS** (Helm)
- Observability: `/healthz` + `/metrics` (Prometheus), Grafana dashboard, Loki logs
- Infra as Code: Terraform for VPC/EKS/IAM

## Goals (v0.1.0)
- Two pages (Home, About) with shared layout
- Route tests pass (/, /about, /healthz)
- Production Dockerfile (non-root, multi-stage)
- Jenkins pipeline builds & pushes image on `develop`
- Helm chart deploys to **dev** namespace with probes
- Tag `v0.1.0` from `main` → promote to **prod**

## Repo layout (planned)