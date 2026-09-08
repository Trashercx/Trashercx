<!-- HEADER: ESTRUCTURA A DOS COLUMNAS CON TU GIF -->
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td width="60%" valign="middle" align="left">
      <a href="https://git.io/typing-svg">
        <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=A970FF&vCenter=true&width=600&lines=Ingeniero+de+Sistemas+%7C+Backend;Arquitecto+Cloud+(AWS+%7C+Azure+%7C+GCP);Auditor%C3%ADa+IT+y+Seguridad+(ISO+27001);IoT+&+Automatización+de+Sistemas" alt="Roles" />
      </a>
      <br>
      <p style="font-size: 16px;">
        Diseñando infraestructura en la nube escalable, desarrollando lógica de negocio robusta y conectando el mundo físico mediante IoT.
      </p>
      <p>
        <a href="https://linkedin.com/in/tu-perfil">
          <img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=00B4DB"/>
        </a>
        <a href="mailto:tu-correo@email.com">
          <img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=A970FF"/>
        </a>
      </p>
    </td>
    <td width="40%" align="center" valign="middle">
      <!-- AQUÍ ESTÁ INTEGRADO TU GIF LOCAL -->
      <img src="gif1.gif" width="90%" style="border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);" alt="Animación Tech" />
    </td>
  </tr>
</table>

<br>

---

### <img src="https://api.iconify.design/lucide/layers.svg?color=%2300B4DB" width="24" style="vertical-align: middle;"> Ecosistema Tecnológico

<div align="center">
  <img src="https://skillicons.dev/icons?i=aws,azure,gcp,linux,docker,php,laravel,mysql,raspberrypi,figma,postman,git&theme=dark&perline=12" alt="Tech Stack" />
</div>

<br>

---

### <img src="https://api.iconify.design/lucide/cpu.svg?color=%23A970FF" width="24" style="vertical-align: middle;"> Arquitectura: Sistema IoT de Asistencia

<p>Modelo conceptual del ecosistema de automatización y gestión de personal (Hardware, Backend y Cloud):</p>

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
