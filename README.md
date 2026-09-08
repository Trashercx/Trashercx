<div align="center">
  <!-- Banner Superior -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:002D62,100:A970FF&height=200&section=header&text=Enterprise%20Cloud%20Platform&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%"/>

  <!-- Subtítulo Animado -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1000&color=00B4DB&center=true&vCenter=true&random=false&width=800&lines=Cloud+Engineering+Platform;Multi-Cloud:+Azure+%7C+AWS+%7C+GCP;Infrastructure+as+Code+(IaC);DevOps+Automation+&+Security" alt="Typing SVG" />
  </a>
  
  <p><i>Solución nativa de la nube moderna, escalable, segura y de alta disponibilidad.</i></p>

  <!-- Insignias de Estado y Tecnologías (Homogeneizadas) -->
  <p align="center">
    <img src="https://img.shields.io/badge/Azure-0D1117?style=for-the-badge&logo=microsoftazure&logoColor=00B4DB&borderColor=002D62"/>
    <img src="https://img.shields.io/badge/AWS-0D1117?style=for-the-badge&logo=amazonaws&logoColor=A970FF&borderColor=A970FF"/>
    <img src="https://img.shields.io/badge/GCP-0D1117?style=for-the-badge&logo=googlecloud&logoColor=00B4DB&borderColor=002D62"/>
    <img src="https://img.shields.io/badge/Kubernetes-0D1117?style=for-the-badge&logo=kubernetes&logoColor=A970FF&borderColor=A970FF"/>
    <img src="https://img.shields.io/badge/Terraform-0D1117?style=for-the-badge&logo=terraform&logoColor=00B4DB&borderColor=002D62"/>
  </p>
</div>

---

### <img src="https://api.iconify.design/lucide/target.svg?color=%23A970FF" width="24" style="vertical-align: middle;"> Resumen del Proyecto

Este repositorio contiene el código fuente y la configuración de una plataforma cloud enfocada en resiliencia y automatización. Los pilares principales son:

- **Escalabilidad y Alta Disponibilidad (HA)**
- **Seguridad y Segmentación de Red** (Implementación de políticas Zero-Trust)
- **Automatización CI/CD**
- **Observabilidad Integral**
- **Optimización de Costos** (FinOps)

<div align="center">
  <br>
  <img src="https://skillicons.dev/icons?i=azure,aws,gcp,terraform,kubernetes,docker,github,linux,prometheus,grafana&theme=dark" alt="Tech Stack" />
  <br><br>
</div>

---

### <img src="https://api.iconify.design/lucide/share-2.svg?color=%23A970FF" width="24" style="vertical-align: middle;"> Arquitectura del Sistema

```mermaid
graph TD
    Client([Internet / Usuarios]) --> WAF[Web Application Firewall]
    WAF --> LB[Load Balancer]
    
    subgraph Kubernetes Cluster [Clúster Kubernetes Multi-Zona]
        LB --> API[API Gateway / Ingress]
        API --> SvcA(Microservicio A)
        API --> SvcB(Microservicio B)
        API --> SvcC(Microservicio C)
    end
    
    subgraph Data Layer [Capa de Persistencia]
        SvcA --> DB1[(Primary Database)]
        SvcB --> Cache[(Redis Cache)]
        DB1 -.-> DB2[(Read Replica)]
    end
    
    style Kubernetes Cluster fill:#0D1117,stroke:#A970FF,stroke-width:2px,color:#fff
    style Data Layer fill:#0D1117,stroke:#00B4DB,stroke-width:2px,color:#fff
