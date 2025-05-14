
# NT533 - Distributed Computing Project (OpenFaaS on K3s)

## Overview
This repository contains the project for the Distributed Computing course (**NT533**) at the University of Information Technology - VNUHCM. The project involves deploying a Function-as-a-Service (FaaS) platform using **OpenFaaS** on a lightweight Kubernetes distribution (**K3s**).

**Instructor:** Th.S Bùi Thanh Bình  
**Academic Year:** 2024 - 2025  

### Team Members
- Nguyễn Võ Đại Dương (22520308)
- Lê Hữu Khánh (22520636)
- Bùi Quốc Minh (22520855)
- Võ Huỳnh Kiều Ngân (22520938)

## Table of Contents
- [Project Goals](#project-goals)
- [Architecture](#architecture)
- [Technologies and Tools](#technologies-and-tools)
- [Implemented Features](#implemented-features)
- [Installation](#installation)
- [Monitoring](#monitoring)
- [References](#references)

## Project Goals
The primary objectives of this project are:

- Understanding the architecture and operation principles of FaaS and serverless computing.
- Deploying OpenFaaS on a K3s Cluster in Google Cloud Platform.
- Building serverless functions (currency exchange, stock tracking, GitLab webhooks).
- Establishing monitoring for OpenFaaS using Prometheus and Grafana.

## Architecture
The system utilizes OpenFaaS deployed on a K3s Cluster (1 master, 2 worker nodes). It includes:

- OpenFaaS Gateway: Central controller for managing functions.
- Serverless Functions: Deployed as containers.
- Monitoring Stack: Prometheus and Grafana for performance tracking.
- Frontend Web Interface: Built with HTML, Tailwind CSS, and JavaScript.

## Technologies and Tools
- **Container Orchestration:** Kubernetes (K3s)
- **Serverless Platform:** OpenFaaS
- **Monitoring:** Prometheus, Grafana
- **Cloud Infrastructure:** Google Cloud Platform
- **CI/CD & Automation:** GitLab, GitLab Webhooks
- **CLI Tools:** arkade, faas-cli, kubectl, Docker
- **Frontend Deployment:** Vercel

## Implemented Features
### 1. Currency Converter
- Converts currencies using ExchangeRate-API.

### 2. Stock Tracker
- Provides real-time stock data via AlphaVantage API.

### 3. GitLab Webhook Integration
- Receives GitLab events and sends notifications to Telegram.

### 4. Monitoring
- Real-time system monitoring using Prometheus and Grafana.

## Installation
Scripts and configurations for setting up the cluster, installing OpenFaaS, and exposing services are available in the [`functions`](./functions/) directory.

## Monitoring
Prometheus and Grafana configurations are included to provide robust system metrics and visualization.

## References
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [K3s Documentation](https://k3s.io/)
- [OpenFaaS Documentation](https://docs.openfaas.com/)
- [Arkade CLI](https://github.com/alexellis/arkade)
- [GitLab Webhooks](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)
