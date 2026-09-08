<div align="center">
  <!-- BANNER SUPERIOR CON PALETA ESTRICTA -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:002D62,100:A970FF&height=180&section=header&text=Oscar%20Ivan&fontSize=55&fontColor=ffffff&animation=fadeIn" width="100%"/>

  <!-- ROLES PROFESIONALES ANIMADOS -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1000&color=00B4DB&center=true&vCenter=true&random=false&width=800&lines=Ingeniero+de+Sistemas+%7C+Backend+Developer;Arquitecto+Cloud+(AWS+%7C+Azure+%7C+GCP);Auditor%C3%ADa+IT+y+Seguridad+(ISO+27001);IoT+&+Automatización+de+Sistemas" alt="Roles" />
  </a>
  
  <p><i>Diseñando infraestructura en la nube escalable, lógica de negocio robusta y conectando el mundo físico mediante IoT.</i></p>

  <!-- ENLACES DE CONTACTO PREMIUM -->
  <p align="center">
    <a href="https://linkedin.com/in/tu-perfil">
      <img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=00B4DB&borderColor=002D62"/>
    </a>
    <a href="mailto:tu-correo@email.com">
      <img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=A970FF&borderColor=A970FF"/>
    </a>
  </p>
</div>

<br>

---

### <img src="https://api.iconify.design/lucide/layers.svg?color=%23A970FF" width="24" style="vertical-align: middle;"> Ecosistema Tecnológico

<div align="center">
  <img src="https://skillicons.dev/icons?i=aws,azure,gcp,linux,docker,php,laravel,mysql,raspberrypi,figma,postman,git&theme=dark&perline=12" alt="Tech Stack" />
</div>

<br>

---

### <img src="https://api.iconify.design/lucide/cpu.svg?color=%23A970FF" width="24" style="vertical-align: middle;"> Arquitectura Destacada: Sistema IoT de Asistencia

Como muestra de mi enfoque integral (Hardware -> Backend -> Cloud), presento la arquitectura conceptual de mi proyecto de automatización y gestión de personal:

```mermaid
graph TD
    subgraph EdgeLayer [Capa Física & IoT]
        Scanner[Lector QR] --> Pi(Raspberry Pi Zero 2 W)
    end
    
    subgraph BackendLayer [Capa de Lógica - Laravel]
        Pi -->|API REST / JSON| API[API Gateway]
        API --> Auth{Validación / Auth}
        Auth -->|Token Válido| Controller(Controlador de Asistencia)
        Controller --> Eloquent[ORM]
    end
    
    subgraph DataLayer [Capa de Datos & Nube]
        Eloquent --> DB[(MySQL Database)]
        Controller -.->|Logs & Auditoría| CloudMon[Cloud Monitoring]
    end
    
    style EdgeLayer fill:#0D1117,stroke:#00B4DB,stroke-width:2px,color:#fff
    style BackendLayer fill:#0D1117,stroke:#A970FF,stroke-width:2px,color:#fff
    style DataLayer fill:#0D1117,stroke:#002D62,stroke-width:2px,color:#fff
