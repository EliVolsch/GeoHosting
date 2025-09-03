# Service Level Agreement (SLA)

![GHSlogo](https://kartoza.com/files/GSH%20Logo.png)

## Kartoza Hosting and SaaS Services

This Service Level Agreement (“SLA”) is entered into by and between:

1. **Kartoza (Pty) Ltd** (“Hosting Provider”), a company incorporated under the
   laws of South Africa, and

2. **[Client Name]** (“Client”), whose details are specified in the associated
   Hosting Service Agreement.

This SLA governs the provision of hosting and SaaS services and outlines the
Hosting Provider’s obligations, Client responsibilities, service levels,
dispute resolution, and limitations of liability.

---

## 1. Definitions

1.1 **“Service”**: The hosting and SaaS services provided by the Hosting
Provider as outlined in the Hosting Agreement.

1.2 **“Uptime”**: The percentage of total time within a calendar month during
which the Service is fully operational, excluding Excluded Downtime.

1.3 **“Excluded Downtime”**: Includes the following:

- **Scheduled Maintenance**: Maintenance activities announced at least 48 hours
  in advance.
- **Emergency Maintenance**: Urgent maintenance required to address critical
  security vulnerabilities or outages.
- **Force Majeure Events**: Circumstances beyond the Hosting Provider’s
  reasonable control (see Section 3).
- **Client-Caused Issues**: Downtime caused by the Client’s misuse,
  unauthorized changes, or third-party integrations.

1.4 **“RTO (Recovery Time Objective)”**: The maximum time allowed to restore
services after a major disruption.

1.5 **“RPO (Recovery Point Objective)”**: The maximum allowable data loss
period based on the frequency of backups.

1.6 **“Confidential Information”**: Any information disclosed by one party to
the other in connection with this SLA, marked as confidential or which a
reasonable person would consider confidential.

---

## 2. Service Level Commitments

2.1 **Uptime Expectation**:  
The Hosting Provider aims to provide a high level of service availability.

2.2 **Service Metrics**:  
The Hosting Provider guarantees the following additional performance metrics:

- **Latency**: Average response time for server requests shall not exceed 200ms
  under normal operating conditions.
- **Bandwidth**: A minimum bandwidth of 1000 Mbps will be maintained for all
  hosted connections.

2.3 **Incident Prioritization and Response Times**:  
Incidents are categorized as follows, with corresponding response and
resolution times:

| **Priority** | **Definition**                    | **Response Time**         | **Resolution Time**        |
|--------------|-----------------------------------|---------------------------|----------------------------|
| Critical     | Service completely unavailable    | 1 business day (SAST)     | Best efforts               |
| High         | Severe degradation of services    | 1 business day (SAST)     | Best efforts               |
| Medium       | Minor issues or degraded services | 1 business day (SAST)     | Best efforts               |
| Low          | Non-urgent issues or queries      | 2 business days (SAST)    | Best efforts               |

2.4 **Disaster Recovery**:

- **RTO**: Restoration of services within 1 business day.
- **RPO**: Data restored to within 1 business day of the last backup (our database
  backups are made nightly).

2.5 **Performance Disclaimer**:  
The Hosting Provider does not warrant that the Service will be uninterrupted or
error-free and shall not be liable for downtime resulting from circumstances
beyond its reasonable control.

---

## 3. Exclusions

The SLA does not apply to:

- **Scheduled Maintenance**: Activities announced at least 48 hours in advance.
- **Emergency Maintenance**: Security patches or urgent repairs that may not
  include advance notice.
- **Client Misuse**: Downtime caused by the Client’s misconfigurations,
  unauthorized use, or failure to comply with requirements.
- **Third-Party Providers**: Outages or performance issues originating from
  third-party integrations, plugins, or hosting dependencies outside the
  Hosting Provider’s control.
- **Force Majeure**: Events beyond reasonable control, such as natural
  disasters, government actions, or cyberattacks.

---

## 4. Data Protection and Security

4.1 **Compliance with Data Laws**:

- **South Africa**: The Hosting Provider complies with the Protection of
  Personal Information Act (POPIA) and all related privacy laws.
- **Portugal**: The Hosting Provider complies with the General Data Protection
  Regulation (GDPR) and related EU directives.

4.2 **Encryption Standards**:

- Data in transit is encrypted using TLS 1.2 or higher.
- Data at rest is encrypted using AES-256 encryption or an equivalent standard.

4.3 **Data Backup Policy**:

- Full backups of all Client data are performed every 24 hours.
- Backups are retained for a period of 30 days.
- Restoration requests initiated by the Client will be processed within 24
  hours.

4.4 **Ownership and Portability**:

- The Client retains full ownership of their data.
- Upon termination, the Hosting Provider will provide the Client with a
  complete export of their data in a mutually agreed format within 30 days.

4.5 **Indemnity**:  
The Client shall indemnify and hold harmless the Hosting Provider against any
claims arising from the misuse of data or unauthorized access to the Client’s
systems.

---

## 5. Acceptable Use Policy and Right of Refusal/Termination

5.1 **Acceptable Use Policy (AUP)**:  
The Client agrees to abide by GeoSpatialHosting's Acceptable Use Policy, which is incorporated herein by reference and may be updated from time to time without prior notice. The AUP strictly prohibits the use of GeoSpatialHosting's services for any illegal activities, distribution of malware, engagement in hacking attempts, spamming, intellectual property infringement, defamation, harassment, or any other activity deemed harmful or detrimental to GeoSpatialHosting or its users..

5.2 **Right of Refusal and Termination**:  
GeoSpatialHosting reserves the absolute right, in its sole discretion, to refuse service to any potential client or to suspend or terminate services for any existing client found to be in violation of this SLA, including but not limited to the AUP. GeoSpatialHosting may take such action immediately and without prior notice in cases of severe violations, particularly those involving illegal activities or significant harm to GeoSpatialHosting's network or reputation. In the event of service termination due to a violation of this SLA, the Client shall not be entitled to any refund of fees paid. GeoSpatialHosting shall not be liable for any damages or losses incurred by the Client or any third party as a result of such suspension or termination.

5.3 **Indemnification**:  
The Client agrees to indemnify, defend, and hold harmless GeoSpatialHosting, its officers, directors, employees, and agents from and against any and all claims, damages, losses, liabilities, costs, and expenses (including reasonable attorneys' fees) arising from or in any way related to the Client's use of the services, content hosted by the Client, any breach of this SLA by the Client, or any act or omission of the Client.

---

## 6. Limitations of Liability

6.1 The Hosting Provider’s total liability under this SLA shall not exceed the
fees paid by the Client in the preceding 3 months.

6.2 The Hosting Provider shall not be liable for:

- Indirect, incidental, or consequential damages, including loss of profits,
  revenue, or data.
- Damages arising from third-party dependencies or Client-caused issues.

6.3 Liability for data breaches caused by malicious attacks is limited to
reasonable efforts to mitigate the breach.

6.4 Disputes shall be resolved via arbitration in Cape Town, South Africa with
each party bearing its own legal costs.

---

## 7. Governing Law and Jurisdiction

7.1 This SLA shall be governed by South African law for services rendered by
Kartoza (Pty) Ltd.

7.2 Any disputes shall be subject to binding arbitration under the rules of the
relevant jurisdiction.

---

## 8. Acceptance

Both parties agree to the terms of this SLA by signing below. The Hosting
Provider entity applicable to this SLA must be selected by marking the checkbox
in the appropriate column.

| Hosting Provider (South Africa)  | Client                                     |
|----------------------------------|--------------------------------------------|
| ☐ Kartoza (Pty) Ltd              | [Client Name]                              |
| Company Number: 2014/109067/07   |                                            |
| Registered Office:               |                                            |
| 1st Floor, Block B, North Park,  | Client Address: [Client Address]           |
| Black River Park, 2 Fir Street,  | Signature: [Signature]                     |
| Observatory, Cape Town, 7925, SA | Date: [Date]                               |