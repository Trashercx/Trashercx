<div align="center">
  <!-- BANNER SUPERIOR -->
  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:002D62,100:A970FF&text=CLOUD%20PLATFORM&fontSize=50&fontColor=ffffff&animation=fadeIn" width="100%" />

  <!-- SUBTÍTULO ANIMADO -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1500&color=00B4DB&center=true&vCenter=true&width=800&lines=Azure+Cloud+Architect;AWS+Solutions+Engineer;Terraform+Automation;Kubernetes+Platform;DevOps+%26+Platform+Engineering;Cloud+Native+Solutions" alt="Typing SVG" />
  </a>

  <br><br>

  <!-- INSIGNIAS DE TECNOLOGÍA -->
  <p align="center">
    <img src="https://img.shields.io/badge/Azure-0D1117?style=for-the-badge&logo=microsoftazure&logoColor=00B4DB&borderColor=002D62" />
    <img src="https://img.shields.io/badge/AWS-0D1117?style=for-the-badge&logo=amazonaws&logoColor=A970FF&borderColor=A970FF" />
    <img src="https://img.shields.io/badge/GCP-0D1117?style=for-the-badge&logo=googlecloud&logoColor=00B4DB&borderColor=002D62" />
    <img src="https://img.shields.io/badge/Terraform-0D1117?style=for-the-badge&logo=terraform&logoColor=A970FF&borderColor=A970FF" />
    <img src="https://img.shields.io/badge/Kubernetes-0D1117?style=for-the-badge&logo=kubernetes&logoColor=00B4DB&borderColor=002D62" />
  </p>
</div>

---

### <img src="https://api.iconify.design/lucide/info.svg?color=%23A970FF" width="26" style="vertical-align: text-bottom;"> About The Platform

This repository contains an enterprise-grade cloud platform designed to deliver scalable, secure and automated cloud-native services.

**Key Objectives:**
*   ✅ Infrastructure as Code
*   ✅ Platform Engineering
*   ✅ Security by Design
*   ✅ Cloud Governance
*   ✅ High Availability & Observability

---

### <img src="https://api.iconify.design/lucide/layers.svg?color=%23A970FF" width="26" style="vertical-align: text-bottom;"> Technology Stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=azure,aws,gcp,terraform,kubernetes,docker,github,linux,prometheus,grafana,git&theme=dark" alt="Stack" />
</div>

<br>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&pause=1000&color=A970FF&center=true&width=800&lines=Building+Cloud+Native+Architectures;Automating+Infrastructure;Improving+Reliability;Enhancing+Cloud+Security;Optimizing+Operational+Processes" />
</div>

---

### <img src="https://api.iconify.design/lucide/network.svg?color=%23A970FF" width="26" style="vertical-align: text-bottom;"> Cloud Architecture

```mermaid
graph TD
    Client([Internet / Client]) --> AppGW[Azure App Gateway]
    
    subgraph AKS_Cluster [Azure Kubernetes Service]
        AppGW --> Pods(Microservices / Pods)
    end
    
    subgraph Security_Layer [Security & Identity]
        Pods --> MI{Managed Identity}
        MI --> KV[Azure Key Vault]
    end
    
    subgraph Observability [Monitoring & Logs]
        Pods -.-> AM[Azure Monitor / Log Analytics]
        AM -.-> Grafana[Grafana Dashboards]
    end

    style AKS_Cluster fill:#0D1117,stroke:#A970FF,stroke-width:2px,color:#fff
    style Security_Layer fill:#0D1117,stroke:#00B4DB,stroke-width:2px,color:#fff
    style Observability fill:#0D1117,stroke:#002D62,stroke-width:2px,color:#fff
