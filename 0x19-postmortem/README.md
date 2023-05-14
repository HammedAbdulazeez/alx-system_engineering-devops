# 0x19-postmortem

### Issue Summary:
There was an outage of Web Application on May 1st May, 2023 from 9:00 AM - 11:00 AM (UTC-5)
Impact: The web application was completely down, and users were unable to access the service during the outage. Approximately 85% of the users were affected.

Root Cause:
The root cause of the outage was a misconfigured load balancer. The load balancer was inadvertently configured to route all traffic to a single server, causing it to become overwhelmed and eventually fail.

### Timeline:

9:00 AM: The issue was detected by a monitoring alert that indicated a sudden spike in traffic to one of the servers.
9:05 AM: The team investigated the server and discovered that it was overloaded with traffic.
9:15 AM: The team attempted to rebalance the traffic load, but the issue persisted.
9:30 AM: The team realized that the load balancer was misconfigured and began investigating the configuration.
10:00 AM: The team identified the root cause as a misconfigured load balancer and began working on a fix.
10:45 AM: The team implemented the fix and tested the system.
11:00 AM: The system was fully restored and operational.
Misleading Investigation/Debugging Paths:
Initially, the team assumed that the sudden spike in traffic was due to a DDoS attack. As a result, they spent significant time investigating this possibility before realizing that the load balancer was misconfigured.

### Escalation:
The incident was initially handled by the on-call engineer. As the issue persisted and it became clear that the root cause was a misconfigured load balancer, the incident was escalated to the senior infrastructure engineer for further investigation and resolution.

### Resolution:
The misconfigured load balancer was fixed by updating its configuration to properly distribute traffic across all servers. Additionally, the team implemented additional monitoring and alerts to catch similar issues in the future.

### Root Cause and Resolution:
The root cause of the outage was the misconfiguration of the load balancer, which caused it to route all traffic to a single server. To fix the issue, the load balancer was reconfigured to distribute traffic across all servers properly.

### Corrective and Preventative Measures:

### Review and update the load balancer configuration to ensure proper traffic distribution.
Implement additional monitoring and alerts to catch similar issues in the future.
Conduct regular reviews of system configurations to prevent similar misconfigurations from occurring.
In conclusion, the outage was caused by a misconfigured load balancer, which was fixed by updating its configuration to properly distribute traffic. The team learned the importance of thorough investigation and reviewing system configurations to prevent similar issues in the future. By implementing additional monitoring and conducting regular reviews, the team can ensure that the system remains stable and operational.
