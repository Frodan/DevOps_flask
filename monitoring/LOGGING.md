# Logging Report
Configurations were made with help of:
https://raw.githubusercontent.com/grafana/loki/v2.3.0/production/docker-compose.yaml
https://github.com/black-rosary/loki-nginx

# Best Practices
- When creating a new dashboard, make sure it has a meaningful name
- Do log rotation
- Use one format for logs
- Upload logs to storage, like s3

# Screenshots
- Working Grafana
  ![](screenshots/grafana.png) 

- Working Loki
  ![](screenshots/app_logs.png) 

- Docker ps lab 7
  ![](screenshots/docker_ps.png) 

- Working Prometheus
  ![](screenshots/prometheus.png) 

- First Dashboard
  ![](screenshots/dashboard_1.png)
 
- Second Dashboard
  ![](screenshots/dashboard2.png)

- Logs From All containers
  ![](screenshots/logs_from_all_containers.png)
