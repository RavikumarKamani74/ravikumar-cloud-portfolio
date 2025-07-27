# ravikumar-cloud-portfolio
=======
# 🌩️ Ravikumar Cloud Portfolio

This project is part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/), built and deployed using AWS serverless services and Infrastructure as Code (IaC) practices. It showcases my skills in cloud architecture, DevOps, CI/CD, and monitoring.

## 🚀 Live Demo

🔗 [https://d20dywo6lz1slm.cloudfront.net](https://d20dywo6lz1slm.cloudfront.net/Frontend/index.html))

---

## 🧠 Key Features

- ✅ **Resume Hosting**: Static resume served via **Amazon S3 + CloudFront**
- ✅ **Visitor Counter**: Real-time tracking using **API Gateway + Lambda + DynamoDB**
- ✅ **Infrastructure as Code**: Entire infrastructure is defined in **AWS CloudFormation**
- ✅ **CI/CD Pipeline**: Automated deployment using **GitHub Actions + IAM OIDC + CodeBuild + CodePipeLine + CodeDeploy**
- ✅ **Monitoring & Alerts**: **CloudWatch Alarms** and **SNS notifications**
- ✅ **Secure & Scalable**: Built on a fully serverless architecture

---

## 🧱 Architecture Overview

User ⇨ CloudFront ⇨ S3 (HTML) / API Gateway ⇨ Lambda ⇨ DynamoDB
⇘ CloudWatch + SNS (Alerts)


---

## 🛠️ Tech Stack

| Service             | Purpose                          |
|---------------------|----------------------------------|
| **S3**              | Static hosting for resume        |
| **CloudFront**      | Global CDN + HTTPS               |
| **API Gateway**     | REST API for visitor counter     |
| **Lambda**          | Serverless function (Python)     |
| **DynamoDB**        | NoSQL counter storage            |
| **CloudFormation**  | Infrastructure as Code (IaC)     |
| **GitHub Actions**  | CI/CD pipeline                   |
| **SNS + CloudWatch**| Monitoring and alerts            |

---

## 📁 Project Structure

├── templates/
│ ├── lambda.yaml
│ ├── dynamodb.yaml
│ ├── api-gateway.yaml
│ ├── s3-cloudfront.yaml
│ ├── sns-alarm.yaml
│ ├── iam.yaml
│ └── parameters.yaml
├── .github/workflows/
│ └── deploy.yml
├── lambda/
│ └── lambda_function.py
├── index.html
├── resume.pdf
└── README.md


---

## 📄 How to Deploy

1. Clone this repo  
2. Set up GitHub OIDC IAM role  
3. Push to `main` → triggers GitHub Actions  
4. Visit CloudFront URL

---

## 🧑‍💻 About Me

**Kamani Ravikumar**  
Cloud/DevOps Engineer | AWS Enthusiast  
[GitHub](https://github.com/RavikumarKamani74) | [Email](mailto:ravikamani789@gmail.com)

---

## 📬 Feedback or Questions?

Feel free to raise an [Issue](https://github.com/RavikumarKamani74/ravikumar-cloud-portfolio/issues) or connect via email.


