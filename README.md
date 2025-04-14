# Technical Task: Deploying a Function App for Compound Interest Calculation

## Scenario

A financial services company wants to provide their customers with a simple compound interest calculator that can be accessed via an HTTP API. They require a serverless solution and have chosen **Azure Functions** as the deployment platform. They have created a Python script that will be deployed to an Azure Function App, which will accept user input via an HTTP request and return the calculated compound interest.

## Task

You are required to create a **DevOps pipeline** that automates the deployment of an Azure Function App. 

Be as **creative** as you can. Flex your Skills!!!

The deployment should include the following components:

### 1. **Infrastructure as Code (IaC)**
Use a tool such as **Bicep**, **Terraform**, or **ARM templates** to provision the necessary Azure resources required for the Function App.

### 2. **CI/CD Pipeline**
Implement a pipeline using a CI/CD tool such as **GitHub Actions**, **Azure DevOps**, or another tool of your choice to automate the deployment of the Function App. This should include:

- Deploying the **Azure Function App**.
- Uploading the provided **Python script** to the Function App.

### 3. **Python Function App**
Deploy the provided Python script to the Azure Function App. The Python function will calculate compound interest based on user input via an HTTP request.

### 4. **Testing**
Show that the HTTP function works by passing a valid HTTP POST.

---

## Provided Python Script
This can be found under function_app.py